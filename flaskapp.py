# Author: Amelia Eibert

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

# ------------------------------
# Route: Home Page
# ------------------------------

@app.route('/')
def home():
    # Query the top 10 movies from the mySQL movie database
    movies = get_top_movies()

    # Convert each row (tuple) into a dictionary for template use
    top_movies = [{'title': row[0], 'popularity': row[1]} for row in movies]

    # Render the template with the list of movies
    return render_template('home_movies.html', top_movies=top_movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)