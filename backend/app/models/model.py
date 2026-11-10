from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    receipts: Mapped[list["Receipt"]] = relationship(back_populates="user")


class Receipt(Base):
    __tablename__ = "receipts"

    receipt_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))  # nullable until auth exists
    store_name: Mapped[str] = mapped_column(String(255))
    number_of_items: Mapped[int]
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped["User | None"] = relationship(back_populates="receipts")
    items: Mapped[list["Item"]] = relationship(back_populates="receipt")


class Item(Base):
    __tablename__ = "items"

    item_id: Mapped[int] = mapped_column(primary_key=True)
    receipt_id: Mapped[int] = mapped_column(ForeignKey("receipts.receipt_id"))
    item_name: Mapped[str] = mapped_column(String(255))
    quantity: Mapped[int]
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    receipt: Mapped["Receipt"] = relationship(back_populates="items")
