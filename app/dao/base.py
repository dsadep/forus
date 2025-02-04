from sqlalchemy import select
from app.database import async_session_maker

class BaseDAO:
    model = None

    @classmethod 
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)  
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod 
    async def get_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=id)  
            result = await session.execute(query)
            return result.mappings().all()