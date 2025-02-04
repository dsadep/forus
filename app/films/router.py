from datetime import date
from fastapi import APIRouter, UploadFile

from app.exceptions import FilmsNotFoundException
from app.films.dao import FilmsDAO
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/films",
    tags=["Фильмы"],
)


@router.get("/")
async def find_all_films():
    result = await FilmsDAO.get_all()
    if not result:
        raise FilmsNotFoundException
    return result

@router.get("/get/{title}")
async def get_films_by_title(title: str):
    result = await FilmsDAO.get_by_title(title)   
    if not result:
        raise FilmsNotFoundException
    return result


@router.get("/view/{title}/{id}")
def main(title: str, id: int):
    def iterfile(): 
        file_path = f"app/films/media/{title}{id}.mp4"
        with open(file_path, mode="rb") as film:
            yield from film  
    return StreamingResponse(iterfile(), media_type="video/mp4")

@router.get("/{id}")
async def get_film(id: int):
    result = await FilmsDAO.get_by_id(id)
    if not result:
        raise FilmsNotFoundException
    return result

@router.post("/upload")
async def add_new_film(
    title: str,
    description: str,
    release_date: date,
):
    new_film = await FilmsDAO.create_new_film(title, description, release_date)
    return new_film