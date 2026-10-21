from importlib import metadata


class MovieMetadata:
    def __init__(self, 
                 director=None, 
                 release_year=None, 
                 cast_members=None):
        self.director = director
        self.release_year = release_year
        self.cast_members = cast_members if cast_members is not None else []

class Movie:
    def __init__(self, movie_id, title, genre, rating, duration, metadata):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.duration = duration
        self.metadata = metadata

class BlockbusterMovie(Movie):
    pass

class ClassicMovie(Movie):
    pass

class Indiemovie(Movie):
    pass

class Showtime:
    def __init__(self, movie, time):
        self.movie = movie
        self.time = time