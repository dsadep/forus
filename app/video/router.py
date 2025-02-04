from fastapi import APIRouter, UploadFile
import shutil
router = APIRouter(
    prefix="/video",
    tags=["Загрузка видео"],
)

@router.post("/add_film")
async def add_film(id: int, title: str, file: UploadFile):
    with open(f"app/films/media/{title}{id}.mp4", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)