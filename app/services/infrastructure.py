from typing import List

from app.models.infrastructure import InfRegionEnum
from app.repositories.infrastructure import InfrastructureRepository
from app.schemas.infrastructure import InfrastructureCreateSchema, InfrastructureOutSchema


class InfrastructureService:
    def __init__(self):
        self.repository: InfrastructureRepository = InfrastructureRepository()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.repository.close()

    async def create(self, data: InfrastructureCreateSchema) -> InfrastructureOutSchema:
        infrastructure_obj = await self.repository.create(data)
        return InfrastructureOutSchema.from_orm(infrastructure_obj)

    async def get_by_id(self, id: int) -> InfrastructureOutSchema | None:
        result = await self.repository.get_by_id(id)
        if result is None:
            return None
        return InfrastructureOutSchema.from_orm(result)

    async def get_by_region(self, region: InfRegionEnum) -> List[InfrastructureOutSchema]:
        result = await self.repository.get_list_by_region(region=region)
        mapped_result = list(map(lambda inf: InfrastructureOutSchema.from_orm(inf), result))
        return mapped_result

    async def get_all(self) -> List[InfrastructureOutSchema]:
        result = await self.repository.get_all()
        mapped_result = list(map(lambda inf: InfrastructureOutSchema.from_orm(inf), result))
        return mapped_result
