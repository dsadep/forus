from sqlalchemy import insert, select
from app.dao.base import BaseDAO
from app.films.models import Films
from app.database import async_session_maker

class FilmsDAO(BaseDAO):
    model = Films

    @classmethod 
    async def get_by_title(cls, title: str):
        async with async_session_maker() as session:
            query = select(Films.__table__.columns).filter(Films.title.ilike(f"%{title}%"))
            result = await session.execute(query)
            return result.mappings().all()
    
    @classmethod 
    async def create_new_film(cls, 
        title: str,
        description: str, 
        release_date: str
    ):
        async with async_session_maker() as session:
            query = insert(Films).values(
                title=title, 
                description=description, 
                release_date=release_date
            ).returning(Films.__table__.columns)

            new_film = await session.execute(query)
            await session.commit()
            return new_film.mappings().one()