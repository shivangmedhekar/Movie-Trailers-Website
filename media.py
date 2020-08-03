# Defining the Movie class
class Movie():

    # Class variable to count the number of instances created
    TOTAL_INSTANCES = 0

    # Defining the constructor, called whenever
    # a new instace of the class is created.
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
        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.protagonist = movie_protagonist
        self.director = movie_director
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        Movie.TOTAL_INSTANCES += 1
