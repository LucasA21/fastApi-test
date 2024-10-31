from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

movies = [
    {
        "id" : 1,
        "title": "Avatar",
        "overview": "En un planeta llamado pandora...",
        "year": "2009",
        "rating": 7.8,
        "category" : "Action"
    },
    {
        "id" : 2,
        "title": "Harry Potter",
        "overview": "En una ciudad magica...",
        "year": "2002",
        "rating": 8.7,
        "category" : "Fantasy"
    },
    {
        "id" : 3,
        "title": "Interestelar",
        "overview": "En una tierra infectada...",
        "year": "2016",
        "rating": 9.2,
        "category" : "Action"
    },
]


app.title = "My first API"

app.version = "0.0.1"


@app.get("/", tags=['Home'])
def home():
    return "Hello world"

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/movies/{id}", tags = ["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
        
@app.get("/movies/", tags = ["Movies"])
def get_movie_category(category: str):
    for movie in movies:
        if movie["category"] == category:
            return movie
        
@app.post("/movies", tags = ["Movies"])
def create_movie(id:int = Body(), 
                 title:str = Body(), 
                 overview:str = Body(), 
                 year:str= Body(),
                 rating:float = Body(),
                 category:str = Body()):
    movies.append(
        {
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category
        }
    )
    return movies


@app.put("/movies/{id}")
def update_movie(
                 id : int,
                 title:str = Body(), 
                 overview:str = Body(), 
                 year:str= Body(),
                 rating:float = Body(),
                 category:str = Body()):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title,
            movie["overview"] = overview,
            movie["year"] = year,
            movie["rating"] = rating,
            movie["category"] = category
    return movies

@app.delete("/movies/{id}", tags = ["Movies"])
def delete_movie(id:int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies