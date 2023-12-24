import random

from model.Movie import Movie


# List of 20 movie instances with example data
class MockMovieList:
    movies_list = [
        Movie(id=1, title="Inception", director="Christopher Nolan", release_year=2010, genres=["Action", "Sci-Fi", "Thriller"], rating=8.8),
        Movie(id=2, title="The Shawshank Redemption", director="Frank Darabont", release_year=1994, genres=["Drama"], rating=9.3),
        Movie(id=3, title="Pulp Fiction", director="Quentin Tarantino", release_year=1994, genres=["Crime", "Drama"], rating=8.9),
        Movie(id=4, title="Fight Club", director="David Fincher", release_year=1999, genres=["Drama"], rating=8.8),
        Movie(id=5, title="Forrest Gump", director="Robert Zemeckis", release_year=1994, genres=["Drama", "Romance"], rating=8.8),
        Movie(id=6, title="The Matrix", director="Lana Wachowski, Lilly Wachowski", release_year=1999, genres=["Action", "Sci-Fi"], rating=8.7),
        Movie(id=7, title="The Godfather", director="Francis Ford Coppola", release_year=1972, genres=["Crime", "Drama"], rating=9.2),
        Movie(id=8, title="The Dark Knight", director="Christopher Nolan", release_year=2008, genres=["Action", "Crime", "Drama"], rating=9.0),
        Movie(id=9, title="Schindler's List", director="Steven Spielberg", release_year=1993, genres=["Biography", "Drama", "History"], rating=8.9),
        Movie(id=10, title="The Lord of the Rings: The Return of the King", director="Peter Jackson", release_year=2003, genres=["Action", "Adventure", "Drama"], rating=8.9),
        Movie(id=11, title="Interstellar", director="Christopher Nolan", release_year=2014, genres=["Adventure", "Drama", "Sci-Fi"], rating=8.6),
        Movie(id=12, title="Gladiator", director="Ridley Scott", release_year=2000, genres=["Action", "Adventure", "Drama"], rating=8.5),
        Movie(id=13, title="The Lion King", director="Roger Allers, Rob Minkoff", release_year=1994, genres=["Animation", "Adventure", "Drama"], rating=8.5),
        Movie(id=14, title="Saving Private Ryan", director="Steven Spielberg", release_year=1998, genres=["Drama", "War"], rating=8.6),
        Movie(id=15, title="Titanic", director="James Cameron", release_year=1997, genres=["Drama", "Romance"], rating=7.8),
        Movie(id=16, title="Goodfellas", director="Martin Scorsese", release_year=1990, genres=["Biography", "Crime", "Drama"], rating=8.7),
        Movie(id=17, title="The Silence of the Lambs", director="Jonathan Demme", release_year=1991, genres=["Crime", "Drama", "Thriller"], rating=8.6),
        Movie(id=18, title="Avatar", director="James Cameron", release_year=2009, genres=["Action", "Adventure", "Fantasy"], rating=7.8),
        Movie(id=19, title="The Prestige", director="Christopher Nolan", release_year=2006, genres=["Drama", "Mystery", "Sci-Fi"], rating=8.5),
        Movie(id=20, title="Back to the Future", director="Robert Zemeckis", release_year=1985, genres=["Adventure", "Comedy", "Sci-Fi"], rating=8.5)
    ]
def get_random_movie():
    return random.choice(MockMovieList.movies_list)