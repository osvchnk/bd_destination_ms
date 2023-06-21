from fastapi import APIRouter

from app.models.infrastructure import InfRegionEnum
from app.schemas.infrastructure import InfrastructureCreateSchema
from app.services.infrastructure import InfrastructureService

router = APIRouter(
    prefix="/infrastructure",
    tags=["infrastructure"]
)


@router.post("")
async def create_infrastructure(data: InfrastructureCreateSchema):
    async with InfrastructureService() as service:
        return await service.create(data)


@router.get("/{id}")
async def get_infrastructure_by_id(id: int):
    async with InfrastructureService() as service:
        return await service.get_by_id(id)


@router.get("")
async def get_all_infrastructures():
    async with InfrastructureService() as service:
        return await service.get_all()


@router.get("?region={region}")
async def get_infrastructure_by_region(region: InfRegionEnum):
    async with InfrastructureService() as service:
        return await service.get_by_region(region)
