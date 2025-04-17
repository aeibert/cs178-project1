# CS 178 Project 1

This project demonstrates how to build a web application using Flask that connects:
- A relational database (SQL) using AWS RDS
- A nonrelational database using AWS DynamoDB

Users can:
- View the most popular movies and genres
- Create and manage user profiles
- Recieve movie recommendations based on their favorite genre

## Technologies Used
- Python
- Flask
- mySQL (using AWS RDS)
- DynamoDB (using AWS)
- boto3 (AWS SDK for Python)
- pymysql (mySQL connector)
- HTML + Bootstrap

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
