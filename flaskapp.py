# Author: Amelia Eibert

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)

# ------------------------------
# Route: Home Page
# ------------------------------

@app.route('/')
def home():
    # Query the top 10 movies from the mySQL movie database
    movies = get_top_movies()

    # Render the template with the list of movies
    return render_template('home_movies.html', top_movies=movies)

# ------------------------------
# Route: Home Page
# ------------------------------

@app.route('/genre')
def genre():
    # Query the most popular genres
    genres = get_top_movie_genres()

    # Render the template with list of movies
    return render_template('genre_movies.html', top_genres = genres)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)