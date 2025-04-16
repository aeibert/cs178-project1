# Author: Amelia Eibert
# Description: 

import pymysql
import pymysql.cursors
import creds 

# ----------------------------------
# Section 1: Connecting to MySQL RDS
# ----------------------------------

def get_conn():

    '''
    Establish and return a connection to the mySQL RDS database using 
    the credentials from creds.py
    '''
    conn = pymysql.connect(
        host= creds.host,
        user= creds.user, 
        password = creds.password,
        db=creds.db,
        cursorclass= pymysql.cursors.DictCursor
        )
    return conn

def execute_query(query, args=()):
    '''
    Execute a SQL Query using a connection to RDS.
    Closes the connection automatically after closing the query
    '''
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows
    finally:
        cur.close()

#----------------------------------
# Section 2: MySQL Queries
#----------------------------------


def get_top_movies():
    '''
    Returns the top Movies from the table,
    including Title, Popularity, and Genre.
    '''
    query = """
        SELECT movie.title, movie.popularity, genre.genre_name 
        FROM movie 
        JOIN movie_genres USING (movie_id)
        JOIN genre USING (genre_id) 
        ORDER BY movie.popularity DESC 
        LIMIT 20
    """

    return execute_query(query)

def get_top_movie_genres():
    '''
    Returns the top 15 genres from the table based on popularity
    '''
    query = """
        SELECT genre.genre_name, SUM(movie.popularity) as total_popularity
        FROM movie 
        JOIN movie_genres USING (movie_id)
        JOIN genre USING (genre_id) 
        GROUP BY genre.genre_name
        ORDER BY movie.popularity DESC 
        LIMIT 15
    """
    return execute_query(query)

def get_movies_by_genre(genre_name):
    '''
    Returns top movies for a specific genre
    I used chatgpt to help write the query so I could get user input
    '''
    query = """
        SELECT movie.title, movie.popularity, genre.genre_name 
        FROM movie 
        JOIN movie_genres USING (movie_id)
        JOIN genre USING (genre_id) 
        WHERE genre.genre_name = %s 
        ORDER BY movie.popularity DESC 
        LIMIT 10
    """
    return execute_query(query, (genre_name,))

def get_all_genres():
    query = "SELECT DISTINCT genre_name FROM genre ORDER BY genre_name"
    return execute_query(query)

#-----------------------------------
# Section 3: Connecting to DynamoDB
#-----------------------------------

import boto3

TABLE_NAME = "Users"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

#-----------------------------------
# Section 4: CRUD - Users
#-----------------------------------

def create_user_profile(username, first_name, genre):
    '''
    Creates a new user profile in the DynamoDB Users table
    '''
    try:
        table.put_item(Item={
            "Username": username,
            "First Name": first_name,
            "Genre": genre
        })
        print("User created successfully.")
    except Exception as e:
        print(f"Error creating user: {e}")

def get_user(username):
    '''
    Retrieves a user profile from the Users table
    '''
    try:
        response = table.get_item(Key={'Username': username})
        return response.get('Item')
    except Exception as e:
        print(f"Error retrieving user: {e}")
        return None

def update_user_genre(username, genre):
    '''
    Updates a user's favorite genre
    '''
    try:
        table.update_item(
            Key={"Username": username},
            UpdateExpression="SET Genre = :g",
            ExpressionAttributeValues={':g': genre}
        )
        print("Genre updated successfully.")
    except Exception as e:
        print(f"Error updating genre: {e}")

def delete_user(username):
    '''
    Deletes a user profile
    '''
    try:
        table.delete_item(Key={"Username": username})
        print("User deleted successfully.")
    except Exception as e:
        print(f"Error deleting user: {e}")



