# Author: Amelia Eibert

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

# ------------------------------
# Route: Home Page for Users
# ------------------------------

@app.route('/')
def home():
    return render_template('home.html')

# ------------------------------
# Route: Top Movie Page
# ------------------------------

@app.route('/movies')
def movies():
    # Query the top 10 movies from the mySQL movie database
    movies = get_top_movies()

    # Render the template with the list of movies
    return render_template('home_movies.html', top_movies=movies)

# ------------------------------
# Route: Top Genre Page
# ------------------------------

@app.route('/genre')
def genre():
    # Query the most popular genres
    genres = get_top_movie_genres()

    # Render the template with list of movies
    return render_template('genre_movies.html', top_genres = genres)


# ------------------------------
# Route: Create User Profile
# ------------------------------

@app.route('/add-user', methods = ['GET', 'POST'] )
def add_user():
    # Creates a new user
    if request.method == 'POST':
        # Extract form data
        username = request.form['Username']
        first_name = request.form['First Name']
        genre = request.form['Genre']

        # Call the function to create the user
        create_user_profile(username, first_name, genre)

        flash('User added successfully!', 'success')
        
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('recommend'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')
    
# ------------------------------
# Route: Read User Profile
# ------------------------------

@app.route('/read-user', methods = ['GET', 'POST'] )
def read_user():
    # Creates a new user
    if request.method == 'POST':
        # Extract form data
        username = request.form['Username']

        # Call the function to get user info
        get_user(username)
        
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('read_user.html')

# ------------------------------
# Route: Update User Profile
# ------------------------------

@app.route('/update-user', methods = ['GET', 'POST'])
def update_user():
    # Updates user's favorite genre
    if request.method == 'POST':

        username = request.form['Username']
        genre = request.form['Genre']

        # Call function to update user 
        update_user_genre(username, genre)

        flash('Favorite genre updated!', 'success')

        return redirect(url_for('home'))
    else:
        return render_template('update_user.html')

# ------------------------------
# Route: Delete User Profile
# ------------------------------
    
@app.route('/delete-user', methods = ['GET', 'POST'])
def delete_user_profile():
    # Updates user's favorite genre
    if request.method == 'POST':

        username = request.form['Username']

        # Call function to update user 
        delete_user(username)

        flash('User deleted :(', 'success')

        return redirect(url_for('home'))
    else:
        return render_template('delete_user.html')
    

# ------------------------------------
# Route: Recommendations based on User
# ------------------------------------
@app.route('/recommend')
def recommend():
    genre = request.args.get('genre')
    movies = get_movies_by_genre(genre)  # You must define this function
    return render_template('recommendations.html', genre=genre, movies=movies)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)