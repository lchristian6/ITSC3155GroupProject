from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    email = Column(String(100))
    phone_number = Column(String(100))
    address = Column(String(100))

    orders = relationship("Order", back_populates="Customer")


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    dishes_id = Column(Integer, ForeignKey("dishes.id"))
    amount = Column(Integer, index=True, nullable=False)

    order = relationship("Order", back_populates="Order_details")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    promo_code = Column(String(50), nullable=True, default=None)

    order_details = relationship("OrderDetail", back_populates="Order")
    customers = relationship("Customer", back_populates="Order")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_information = Column(String(100))
    transaction_status = Column(String(100))
    payment_type = Column(String(100))

    payments = relationship("Payment", back_populates="Payment")


class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pizza_name = Column(String(100))
    price = Column(Integer)
    ingredients = Column(String(100))
    calories = Column(Integer)
    food_category = Column(String(100))

    resources = relationship("Resources", back_populates="Pizzas")


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_type = Column(String(100))
    promotion_code = Column(String(100))
    expiration = Column(Date)

    # orders = relationship("Order", back_populates="customer")


class ResourceManagement(Base):
    __tablename__ = "resource_management"

    id = Column(Integer, primary_key=True, index=True)
    ingredient_name = Column(String(100), index=True)
    amount = Column(Float)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review = Column(String(100))
    score = Column(Integer())

    # reviews = relationship("Review", back_populates="review")
