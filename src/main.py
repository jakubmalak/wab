from typing import List

from fastapi import FastAPI, HTTPException, Body, status
from src.model.Movie import Movie
from src.mock_data import MoviesMock

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


@app.get("/movie/{movie_id}", response_model=Movie)
def get_movie_by_id(movie_id: int):
    # Search for the movie with the given ID
    movie = next((movie for movie in MoviesMock.MockMovieList.movies_list if movie.id == movie_id), None)

    # If the movie is not found, return a 404 error
    if movie is None:
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")

    return movie


@app.delete("/movie/{movie_id}", response_model=Movie)
def delete_movie_by_id(movie_id: int):
    # Search for the movie with the given ID and remove it
    movie_index = next((i for i, movie in enumerate(MoviesMock.MockMovieList.movies_list) if movie.id == movie_id), None)

    if movie_index is None:
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")

    # Remove the movie from the list
    deleted_movie = MoviesMock.MockMovieList.movies_list.pop(movie_index)
    return deleted_movie


@app.post("/movie", response_model=Movie, status_code=status.HTTP_201_CREATED)
def add_movie(movie: Movie = Body(...)):
    # Check if a movie with the same ID already exists
    if any(m.id == movie.id for m in MoviesMock.MockMovieList.movies_list):
        raise HTTPException(status_code=400, detail=f"Movie with id {movie.id} already exists")

    # Add the new movie to the list
    MoviesMock.MockMovieList.movies_list.append(movie)
    return movie
