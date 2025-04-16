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

        # Message banner
        flash('User added successfully!', 'success')
        
        # Redirect to home page or another page upon successful submission
        # I used chatgpt to help fix my issue with this line of code
        return redirect(url_for('recommendations', username=username))

    # Render the form page if the request method is GET
    genres = get_all_genres()
    return render_template('add_user.html', genres=genres)
    

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

        # Successful message banner
        flash('Favorite genre updated!', 'success')

        # Redirect user
        return redirect(url_for('home'))
    else:
        genres = get_all_genres()
        return render_template('update_user.html', genres=genres)

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

        # Message banner
        flash('User deleted :(', 'dark')

        # Redirect user
        return redirect(url_for('home'))
    else:
        return render_template('delete_user.html')
    

# ------------------------------------
# Route: Recommendations based on User
# ------------------------------------

# I also used ChatGPT here to create this route
@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == 'POST':
        # User submitted the form on the homepage
        username = request.form['username']
    else:
        # Username passed as query parameter after profile creation
        username = request.args.get('username')

    if not username:
        flash("No username provided", "warning")
        return redirect(url_for('home'))

    user = get_user(username)
    if user:
        genre = user['Genre']
        movie_recs = get_movies_by_genre(genre)
        return render_template('recommendations.html', genre=genre, movies=movie_recs)
    else:
        flash("User not found", "danger")
        return redirect(url_for('home'))


# ------------------------------------
# Route: Manage User Profile
# ------------------------------------
@app.route('/manage-user')
def manage_user():
    return render_template('manage_user.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)