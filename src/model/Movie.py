from pydantic import BaseModel
# Define a Pydantic model for response serialization
class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int
    genres: list[str]
    rating: float