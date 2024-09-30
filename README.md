# Movie Trailers Website

This project is a **Movie Trailers Website** that showcases details and trailers for selected movies. It generates a visually appealing webpage displaying movie posters, titles, release years, directors, and storylines. Users can click on a movie tile to view the trailer, which plays within a modal on the same page.

## Features

- Displays movie posters, titles, years, directors, and plot summaries.
- Dynamic modal pop-up to watch movie trailers without leaving the page.
- Supports a list of movies, auto-generating HTML to display movie information.
- Responsive and interactive webpage using Bootstrap for styling and jQuery for animations.

## Technologies Used

- **Python**: Backend logic for generating HTML content.
- **HTML/CSS**: For the structure and styling of the webpage.
- **Bootstrap**: For responsive design and layout.
- **jQuery**: For modal pop-up and animation effects.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shivangmedhekar/Movie-Trailers-Website.git
   cd Movie-Trailers-Website
   ```

2. **Run the Python script**:
   Execute the `entertainment_center.py` file to generate and launch the movie trailers webpage.
   ```bash
   python entertainment_center.py
   ```

3. **View the Webpage**:
   The webpage will automatically open in your default browser. You can view the movie details and play trailers directly from the site.

## Adding Movies

To add more movies, modify the `entertainment_center.py` file by creating new instances of the `Movie` class and appending them to the `movies` list.

Example:
```python
new_movie = media.Movie(
            "Movie Title",
            "Movie storyline...",
            "Genre",
            "Main Actor",
            "Director",
            "Release Year",
            "Poster Image URL",
            "YouTube Trailer URL")

movies.append(new_movie)
```

## Project Structure

- **entertainment_center.py**: Main script that initializes movie instances and generates the webpage.
- **fresh_tomatoes.py**: Contains HTML templates and functions to generate the movie tiles and display the webpage.
- **media.py**: Defines the `Movie` class to represent each movie and track the total number of movies.

## Future Enhancements

- Add more customization options for movie display (e.g., filters by genre or year).
- Improve the UI with additional animations and interactive features.
- Integrate a database for dynamic movie storage.

## License

This project is licensed under the MIT License.

---

Enjoy browsing your favorite movie trailers with this interactive website!
