import media
import fresh_tomatoes

# Creating the instance of the Movie class
batman_begins = media.Movie(
            "Batman Begins",
            "Batman Begins is a 2005 superhero film directed by Christopher Nolan and written by Nolan and David S. Goyer. Based on the DC Comics character Batman, it stars Christian Bale, Michael Caine, Liam Neeson, Katie Holmes, Gary Oldman, Cillian Murphy, Tom Wilkinson, Rutger Hauer, Ken Watanabe, and Morgan Freeman.",
            "Action", "Christian Bale", "Christopher Nolan", "2005",
            "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
            "https://youtu.be/xXqCS-DBKAQ") 

dark_knight = media.Movie(
            "The Dark Knight",
            "The Dark Knight Rises is a 2012 superhero film directed by Christopher Nolan, who co-wrote the screenplay with his brother Jonathan Nolan, and the story with David S. Goyer.[5] Based on the DC Comics character Batman, it is the final installment in Nolan's The Dark Knight Trilogy, and the sequel to The Dark Knight (2008). Christian Bale stars as Bruce Wayne / Batman, alongside Michael Caine, Gary Oldman, Anne Hathaway, Tom Hardy, Marion Cotillard, Joseph Gordon-Levitt, and Morgan Freeman. ",
            "Drama", "Christian Bale", "Christopher Nolan", "2012",
            "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",  # noqa
            "https://www.youtube.com/watch?v=EXeTwQWrcwY") 

iron_man = media.Movie(
            "Iron Man",
            "IIron Man is a 2008 American superhero film based on the Marvel Comics character of the same name. Produced by Marvel Studios and distributed by Paramount Pictures,[N 1] it is the first film in the Marvel Cinematic Universe. It was directed by Jon Favreau from a screenplay by the writing teams of Mark Fergus and Hawk Ostby, and Art Marcum and Matt Holloway, and stars Robert Downey Jr. as Tony Stark / Iron Man alongside Terrence Howard, Jeff Bridges, Shaun Toub, and Gwyneth Paltrow. In the film, following his escape from captivity by a terrorist group, world famous industrialist and master engineer Tony Stark builds a mechanized suit of armor and becomes the superhero Iron Man.",
            "Action", "	Robert Downey Jr.", "	Jon Favreau", "2008",
            "https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg", 
            "https://www.youtube.com/watch?v=8ugaeA-nMTc") 

# Creating a list containing the instances of the Movie just created
movies = [batman_begins, dark_knight, iron_man]

# Calling the open_movies_page to create the page with the Movies
fresh_tomatoes.open_movies_page(movies, media.Movie.TOTAL_INSTANCES)
