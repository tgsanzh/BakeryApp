from fastapi import APIRouter
from sqlalchemy.orm import Session, joinedload

from Backend.backend.db_depends import get_db
from Backend.models.CartItems import CartItems
from Backend.schemas import *
from Backend.utils import *

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/", response_model=CartItemOut)
def create_cart_item(
    item: CartItemBase,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    db_item = CartItems(user_id=user_id, **item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[CartItemOut])
def read_all_cart_items(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    items = db.query(CartItems)\
        .options(joinedload(CartItems.Products))\
        .filter(CartItems.user_id == user_id).all()
    return items


@router.delete("/{cart_item_id}", response_model=CartItemOut)
def delete_cart_item(
    cart_item_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    db_item = db.query(CartItems).filter(
        CartItems.cart_item_id == cart_item_id,
        CartItems.user_id == user_id
    ).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(db_item)
    db.commit()
    return db_item

@router.put("/{cart_item_id}/change-quantity", response_model=CartItemOut)
def change_cart_item_quantity(
    cart_item_id: int,
    change: CartItemQuantityChange,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    db_item = db.query(CartItems).filter(
        CartItems.cart_item_id == cart_item_id,
        CartItems.user_id == user_id
    ).first()

    if not db_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    if change.action == "plus":
        db_item.quantity += 1
    elif change.action == "minus":
        db_item.quantity -= 1
        if db_item.quantity < 1:
            db.delete(db_item)
            db.commit()
            raise HTTPException(status_code=200, detail="Cart item removed (quantity became 0)")
    else:
        raise HTTPException(status_code=400, detail="Invalid action. Use 'plus' or 'minus'.")

    db.commit()
    db.refresh(db_item)
    return db_item