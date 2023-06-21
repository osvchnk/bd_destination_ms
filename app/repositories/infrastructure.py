from typing import List

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import async_session
from app.models.infrastructure import Infrastructure, InfRegionEnum
from app.schemas.infrastructure import InfrastructureCreateSchema


class InfrastructureRepository:

    def __init__(self):
        self.session: AsyncSession = async_session()

    async def close(self):
        if self.session is not None:
            try:
                await self.session.close()
            except Exception as ex:
                raise ex

    async def create(self, data: InfrastructureCreateSchema) -> Infrastructure:
        infrastructure_object = Infrastructure(**data.dict())
        self.session.add(infrastructure_object)
        await self.session.commit()
        await self.session.refresh(infrastructure_object)
        return infrastructure_object

    async def get_by_id(self, id: int) -> Infrastructure | None:
        return await self.session.get(Infrastructure, id)

    async def get_list_by_region(self, region: InfRegionEnum) -> List[Infrastructure]:
        query = (
            select(Infrastructure).
            filter(Infrastructure.region == region).
            order_by(desc(Infrastructure.id))
        )
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_all(self):
        query = (
            select(Infrastructure).
            order_by(desc(Infrastructure.id))
        )
        result = await self.session.execute(query)
        return result.scalars().all()
