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
    Returns the top 10 Movies from the table,
    including Title and Popularity. Used on the homepage
    '''
    query = "SELECT title, popularity FROM movie ORDER BY popularity DESC LIMIT 10 "

    return execute_query(query)

def get_top_movie_genres():
    '''
    Returns the top 10 movies from the table including title, popularity, and genre
    '''
    query = """
        SELECT movie.title, movie.popularity, genre.genre_name 
        FROM movie 
        JOIN movie_genres USING (movie_id)
        JOIN genre USING (genre_id) 
        ORDER BY movie.popularity DESC 
        LIMIT 10
    """
    return execute_query(query)
