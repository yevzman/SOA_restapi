from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, LargeBinary

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

metadata_object = MetaData()


# ========================== Data Base Tables Metadata ====================================

users_table = Table(
    "users",
    metadata_object,
    Column("user_id", Integer, primary_key=True, nullable=False),
    Column("user_name", String(40), nullable=False),
    Column("gender", String(15), nullable=False),
    Column("image", LargeBinary, nullable=False),
    Column("email", String(40), nullable=False),
)

# ========================= DataBase Mapped Classes Metadata ==============================

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(40), nullable=False)
    gender: Mapped[str] = mapped_column(String(15), nullable=False)
    image: Mapped[LargeBinary] = mapped_column(LargeBinary, nullable=False)
    email: Mapped[str] = mapped_column(String(40), nullable=False)

    def __repr__(self) -> str:
        return f'User(user_id={self.user_id}, user_name={self.user_name})'
