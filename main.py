from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from routers.movie import movie_router
from routers.users import user_router

app = FastAPI()
app.title = "APP con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)
        
@app.get('/', tags=['Home'], dependencies=[Depends(JWTBearer())])
def message():
    return HTMLResponse('<h1> Movies </h1>')


'''
movies = [
    {
        "ids": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": 2009,
        "rating": 7.8,
        "category": "Action"    
    },
    {
        "ids": 2,
        "title": "Inception",
        "overview": "Dom Cobb es un ladrón capaz de adentrarse en los sueños de la gente y hacerse con sus secretos. Sin embargo...",
        "year": 2010,
        "rating": 9.0,
        "category": "Action"    
    },
    {
        "ids": 3,
        "title": "Shrek",
        "overview": "Hace mucho tiempo, en una lejana ciénaga, vivía un ogro llamado Shrek. Un día...",
        "year": 2007,
        "rating": 8,
        "category": "Animation"
    }
  
        ]
''' 
