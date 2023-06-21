from pydantic import BaseModel

from app.models.infrastructure import InfRegionEnum


class InfrastructureCreateSchema(BaseModel):
    name: str
    region: InfRegionEnum
    payment_amount: int
    description: str


class InfrastructureOutSchema(InfrastructureCreateSchema):
    id: int

    class Config:
        orm_mode = True
