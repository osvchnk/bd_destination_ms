import enum

from sqlalchemy import Column, Integer, String, Enum

from app.db import Base


class InfRegionEnum(enum.Enum):
    KRASNODAR = "krasnodar"
    STAVROPOL = "stavropol"
    CRIMEA = "crimea"
    ALTAI = "altai"
    PETESBURG = "petesburg"


class Infrastructure(Base):
    __tablename__ = "infrastructure"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    region = Column(Enum(InfRegionEnum), nullable=False)
    payment_amount = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
