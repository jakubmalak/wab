from typing import List

from fastapi import  FastAPI
from model.Movie import Movie
from mock_data import MoviesMock

app = FastAPI()

my_movie = Movie(
    id=1,
    title="Inception",
    director="Christopher Nolan",
    release_year=2010,
    genres=["Action", "Sci-Fi", "Thriller"],
    rating=8.8
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movie", response_model=Movie)
def get_movie():
    # Convert the Movie object to a dict and return
    return Movie(**MoviesMock.get_random_movie().__dict__)

@app.get("/movies", response_model=List[Movie])
def get_movies():
    # Return the list of all movies
    return MoviesMock.MockMovieList.movies_list