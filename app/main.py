from fastapi import FastAPI
from app.films.router import router as films_router
from app.video.router import router as video_router

app = FastAPI()

app.include_router(films_router)
app.include_router(video_router)