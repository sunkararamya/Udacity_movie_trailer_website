"""Defines the Movie class that contains the details of a movie."""
import webbrowser

class Film(object):
    """This class provides a way to store movie related information."""

    """Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
        release_date: A string to store the release date of the movie.
    """

    def __init__(self, movie_title, movie_theme, poster_url,
                 movietrailer_youtube, film_release_date):
        """Initialises Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_theme
        self.poster_image_url = poster_url
        self.trailer_youtube_url = movietrailer_youtube
        self.release_date = film_release_date

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
