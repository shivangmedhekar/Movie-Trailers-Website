# Defining the Movie class
class Movie():
    """
    A class to represent a movie with its details.
    
    Attributes:
        title (str): The title of the movie.
        storyline (str): A brief description of the movie's plot.
        genre (str): The genre of the movie.
        protagonist (str): The main actor or protagonist of the movie.
        director (str): The director of the movie.
        year (str): The release year of the movie.
        poster_image_url (str): URL to the movie's poster image.
        trailer_youtube_url (str): URL to the movie's trailer on YouTube.
    """

    # Class variable to count the number of instances created
    TOTAL_INSTANCES = 0

    def __init__(
                self,
                movie_title,
                movie_storyline,
                movie_genre,
                movie_protagonist,
                movie_director,
                movie_year,
                poster_image,
                trailer_youtube):
        """
        The constructor for the Movie class.
        
        Args:
            movie_title (str): The title of the movie.
            movie_storyline (str): A brief description of the movie's plot.
            movie_genre (str): The genre of the movie.
            movie_protagonist (str): The main actor or protagonist of the movie.
            movie_director (str): The director of the movie.
            movie_year (str): The release year of the movie.
            poster_image (str): URL to the movie's poster image.
            trailer_youtube (str): URL to the movie's trailer on YouTube.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.protagonist = movie_protagonist
        self.director = movie_director
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        Movie.TOTAL_INSTANCES += 1  # Increment the class variable for each new instance
