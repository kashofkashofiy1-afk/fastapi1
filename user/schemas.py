from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal


class ProductBase(BaseModel):
    title: str
    price: Decimal
    desc: Optional[str] = None
    stock: int
    category_id: int

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True


class ProductCreate(ProductBase):
    name: str

class Product(ProductBase):
    id: int
    class Config:
        from_attributes = True