# Movie-Trailers-Website

This project will build a Movie Trailer Website where users can see my favorite movies and watch the trailers. The code stores a list of movie titles, poster images, and movie trailer, genre, lead actor, director and year of release URLs. This information is displayed on a web page and allow users to review the movies and watch the trailers.

The Movie Class in the media.py module creates a data structure to store your favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.

The entertainment_center.py file creates multiple instances of that Movie Class to represent your favorite movies and groups all the instances together in a list.

The Python module called fresh_tomatoes.py has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.

### Contents of Website
```
Website/
├── entertainment_center.py
├── media.py
└── fresh_tomatoes.py
```

## Requirements
- Python 2.7 or Python 3.x

You can download python [here](https://www.python.org/downloads/).

## Usage:

You should start cloning this repository:

    $ git clone https://github.com/shivangmedhekar/Movie-Trailers-Website.git

After getting the code, you must run **entertainment_center.py** script with **python** like this:
    
    $ cd Website
    $ python entertainment_center.py

This script will create the **fresh_tomatoes.html** and open a web browser for you to show the page.



## Team
|  **Shivang Medhekar** |  **Elton Lemos** | **Abhishek Ghoshal** | **Nivya Jomichan** | **Prim Dsouza** |
| :---: |:---:|:---:| :---:|:---:|
| [![Shivang Medhekar](https://avatars2.githubusercontent.com/u/69140290?s=200&u=5df35a82b6d2b6b7b876dfdc22d451c92d30a5c6&v=4)](https://github.com/shivangmedhekar) | [![Elton Lemos](https://media-exp1.licdn.com/dms/image/C5103AQFG2Cinmyjfbg/profile-displayphoto-shrink_200_200/0?e=1597276800&v=beta&t=RY6KFxrNbAhQeA-dB47A51HoFXjyEj7v1UHYnmAOPo4)](https://github.com/icefrostpeng) |
| <a href="https://github.com/shivangmedhekar" target="_blank">`github.com/shivangmedhekar`</a>| <a href="https://github.com/icefrostpeng" target="_blank">`github.com/icefrostpeng`</a> | 



## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
