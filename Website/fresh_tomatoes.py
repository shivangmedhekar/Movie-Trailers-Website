import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>OSTL Mini Project</title>

    <!-- Bootstrap 3 CSS for styling -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    
    <!-- jQuery and Bootstrap JS for interactive components -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    
    <!-- Custom CSS styles -->
    <style type="text/css" media="screen">
        body {
            padding-top: 80px; /* Space for fixed navbar */
            background-color: black; /* Background color of the page */
        }
        #trailer .modal-dialog {
            margin-top: 200px; /* Positioning the modal vertically */
            width: 640px; /* Width of the modal */
            height: 480px; /* Height of the modal */
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001; /* Ensures the close button is on top */
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px; /* Space below each movie tile */
            padding-top: 20px; /* Space above each movie tile */
            color: white; /* Text color */
        }
        .movie-tile:hover {
            background-color: #EEE; /* Background on hover */
            cursor: pointer; /* Pointer cursor on hover */
            color: black; /* Text color on hover */
        }
        .scale-media {
            padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black; /* Background behind the video */
        }
    </style>
    
    <!-- Custom JavaScript for interactivity -->
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src attribute to stop the video playback
            $("#trailer-video-container").empty();
        });
        
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id'); // Get YouTube ID from data attribute
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1'; // Construct embed URL with autoplay
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext); // Sequentially display movie tiles
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <!-- Close button for the modal -->
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <!-- Container for the trailer video -->
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <!-- Fixed navbar at the top -->
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">OSTL Mini Project: Movie Trailer's Website</a>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Container for all movie tiles -->
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry HTML template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342" alt="{movie_title} - {movie_year}">
    <h2>{movie_title}</h2>
    <p>{movie_year}</p>
    <h4>Directed by <b>{movie_director}</b></h4>
    <p><b>Plot</b>: <i>{movie_storyline}</i></p>
</div>
'''

def create_movie_tiles_content(movies):
    """
    Generate the HTML content for each movie tile.

    Args:
        movies (list): List of Movie instances.

    Returns:
        str: Combined HTML content for all movie tiles.
    """
    # Initialize the content variable
    content = ''
    for movie in movies:
        # Extract the YouTube ID from the trailer URL using regex
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the movie tile with the specific movie's data
        content += movie_tile_content.format(
            movie_title = movie.title,
            movie_storyline = movie.storyline,
            movie_director = movie.director,
            movie_year = movie.year,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id
        )

    return content

def open_movies_page(movies, counter):
    """
    Create or overwrite the output HTML file and open it in the browser.

    Args:
        movies (list): List of Movie instances.
        counter (int): Total number of movie instances.
    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Generate the movie tiles HTML by inserting the movie data
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        movie_counter = counter)  # Note: 'movie_counter' is not used in the template

    # Write the combined HTML content to the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Get the absolute path to the output file
    url = os.path.abspath(output_file.name)
    # Open the output file in the default web browser in a new tab
    webbrowser.open('file://' + url, new=2)
