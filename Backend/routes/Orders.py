from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Backend.backend.db_depends import get_db
from Backend.models.CartItems import CartItems
from Backend.models.OrderItems import OrderItems
from Backend.models.Orders import Orders
from Backend.models.Products import Products
from Backend.models.Users import Users
from Backend.schemas import CreateOrder, UpdateOrderStatus
from Backend.utils import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/")
def create_order(
    delivery_address: CreateOrder,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    cart_items = db.query(CartItems).filter(CartItems.user_id == user_id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_amount = 0
    order = Orders(
        user_id=user_id,
        total_amount=0,  # временно 0, обновим позже
        status="Pending",
        delivery_address=delivery_address.delivery_address,
        created_at=datetime.utcnow()
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in cart_items:
        product = db.query(Products).filter(Products.product_id == item.product_id).first()
        if not product:
            continue
        order_item = OrderItems(
            order_id=order.order_id,
            product_id=product.product_id,
            quantity=item.quantity,
            price=product.price
        )
        total_amount += item.quantity * float(product.price)
        db.add(order_item)

    # обновляем итоговую сумму
    order.total_amount = total_amount
    db.query(CartItems).filter(CartItems.user_id == user_id).delete()  # очищаем корзину

    db.commit()
    db.refresh(order)
    return {"order_id": order.order_id, "total_amount": total_amount}

@router.get("/")
def get_user_orders(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    orders = db.query(Orders).filter(Orders.user_id == user_id).all()

    results = []
    for order in orders:
        order_items = db.query(OrderItems).filter(OrderItems.order_id == order.order_id).all()
        items_detail = []
        for item in order_items:
            product = db.query(Products).filter(Products.product_id == item.product_id).first()
            items_detail.append({
                "product_id": product.product_id,
                "name": product.name,
                "quantity": item.quantity,
                "price": float(item.price)
            })
        results.append({
            "order_id": order.order_id,
            "total_amount": float(order.total_amount),
            "status": order.status,
            "delivery_address": order.delivery_address,
            "created_at": order.created_at,
            "items": items_detail
        })
    return results

@router.put("/{order_id}")
def update_order_status(
    order_id: int,
    status_update: UpdateOrderStatus,
    db: Session = Depends(get_db)
):
    order = db.query(Orders).filter(Orders.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status_update.status
    db.commit()
    return {"message": f"Order {order_id} updated to {status_update.status}"}

@router.get("/admin/all")
def get_all_orders_admin(db: Session = Depends(get_db)):
    orders = db.query(Orders).all()

    result = []
    for order in orders:
        user = db.query(Users).filter(Users.user_id == order.user_id).first()
        order_items = db.query(OrderItems).filter(OrderItems.order_id == order.order_id).all()

        items_data = []
        for item in order_items:
            product = db.query(Products).filter(Products.product_id == item.product_id).first()
            items_data.append({
                "product_id": product.product_id,
                "product_name": product.name,
                "quantity": item.quantity,
                "price_per_item": float(item.price),
            })

        result.append({
            "order_id": order.order_id,
            "user_id": order.user_id,
            "user_phone": user.phone,
            "status": order.status,
            "total_amount": float(order.total_amount),
            "delivery_address": order.delivery_address,
            "created_at": order.created_at,
            "items": items_data,
        })

    return result