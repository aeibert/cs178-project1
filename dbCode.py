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
    including Title, Popularity, and Genre. Used on the homepage
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

def create_user():
    Username = input("Enter the Title of the movie: ")
    Ratings = input("Enter the Ratings for the movie: ")
    Year = input("Enter the Year the movie came out: ")
    Genre = input("Enter the Genre of the movie: ")

    movie = {
        "Title": Title,
        "Ratings": Ratings,
        "Year": Year,
        "Genre": Genre
    }

    response = table.put_item(Item = movie)

    print("creating a movie")