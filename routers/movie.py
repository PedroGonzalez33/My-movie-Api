from fastapi import Path, Query
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from typing import List 
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()

@movie_router.get('/movies', tags=['Get Movies'], response_model= List[Movie], status_code = 200) 
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@movie_router.get('/movies/{ids}', tags=['Get Movies'], response_model= Movie, status_code = 200)
def get_movie(ids: int = Path(gt = 0, le = 2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(ids)
    if result == []:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@movie_router.get('/movies/', tags = ['Get Movies'], response_model= List[Movie],status_code = 200)
def get_movies_by_category(category: str = Query(default = 'Category of the Movie',max_length = 10, min_length = 5)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if result == []:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@movie_router.post('/movies', tags = ['Create Movies'], response_model= dict, status_code = 201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code = 201, content = {"message": "Movie Registed"})

@movie_router.put('/movies/{ids}', tags=['Modificate Movies'], response_model= dict, status_code = 200)
def update_movie(ids: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(ids)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    else:
        MovieService(db).update_movie(ids, movie)
    return JSONResponse(status_code = 200, content = {"message": "Movie Modificated"})

@movie_router.delete('/movies/{ids}', tags=['Delete Movies'], response_model= dict, status_code = 200)
def delete_movie(ids: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(ids)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    else:
       MovieService(db).delete_movie(ids) 
    return JSONResponse(status_code = 200, content = {"message": "Movie Deleted"})