# Author: Amelia Eibert
# Description: 

import pymysql
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
        )
    return conn

def execute_query(query, args=()):
    '''
    Execute a SQL Query using a connection to RDS.
    Closes the connection automatically after closing the query
    '''
    cur = get_conn().cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

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

