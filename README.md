# CS 178 Project 1

This project demonstrates how to build a web application using Flask that connects:
- A relational database (SQL) using AWS RDS
- A nonrelational database using AWS DynamoDB
  
The project uses a MySQL database to store movie data and DynamoDB to store user profiles. It integrates these technologies in a Flask web application deployed on AWS EC2.
Users can explore the most popular movies and genres, create and manage user profiles, and receive personalized movie recommendations based on their favorite genre.

## Getting Started
1. Clone the Repository
   ```
   git clone https://github.com/aeibert/cs178-project1.git
   cd cs178-project1
   ```

3. Install Requirements
   ```
   pip install Flask boto3 pymysql
   ```
5. Create your Creds File
   
   Create a `creds.py` file with the following format
   ```
   # creds.py
   host = 'your-rds-endpoint'
   user = 'admin'
   password = 'your-mysql-password'
   db = 'movies'
   ```
   **Do not** push this file to github. It contains sensitive information.

## AWS Setup Required
- **RDS:** Set up an RDS instance and load the `movies` dataset
- **DynamoDB:** Create a table named `Users` with `Username` as partition key. Include attributes `First Name` and `Genre`
- **IAM Permissions:** User must have permission to access DynamoDB from your code

## Run the app
```
python3 flaskapp.py
```
