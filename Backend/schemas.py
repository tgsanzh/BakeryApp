from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    phone: str

class CategoryOut(BaseModel):
    category_id: int
    name: str

    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    image_url: str
    category_id: int

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    category_id: int

    class Config:
        orm_mode = True

class ProductOutShort(BaseModel):
    product_id: int
    name: str
    price: float
    image_url: str

    class Config:
        orm_mode = True

class CartItemOut(BaseModel):
    cart_item_id: int
    user_id: int
    quantity: int
    Products: ProductOutShort

    class Config:
        orm_mode = True

class CartItemQuantityChange(BaseModel):
    action: str

class CartItemBase(BaseModel):
    product_id: int

class OrderItemOut(BaseModel):
    product: ProductOut
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    order_id: int
    total_amount: float
    status: str
    delivery_address: str
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        orm_mode = True


class RegisterRequest(BaseModel):
    phone: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    phone: str
    password: str

class CreateOrder(BaseModel):
    delivery_address: str

class UpdateOrderStatus(BaseModel):
    status: str
