from datetime import datetime

from dateutil import relativedelta
from sqlalchemy import ForeignKey, Column, String, Integer, Numeric, \
    Boolean,  DateTime
from sqlalchemy.orm import relationships, relationship

from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Numeric)
    desc = Column(String)
    stock = Column(Integer)  

    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="products")


class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    total_price = Column(Numeric)
    status = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    price = Column(Numeric)
    quantity = Column(Integer)
    order = relationship("Order", back_populates="items")
    product = relationship("Product")