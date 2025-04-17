# CS 178 Project 1

This project demonstrates how to build a web application using Flask that connects:
- A relational database (SQL) using AWS RDS
- A nonrelational database using AWS DynamoDB

This app collects user profile info and displays movie recommendations based on the user's favorite genre.

## Getting Started
1. Clone the Repository
2. Install Requirements
3. Create your Creds File
   
   Do not push this file to github. It contains sensitive information.

## AWS Setup Required
- **RDS:** Set up an RDS instance and load the `movies` dataset
- **DynamoDB:** Create a table named `users` with `Username` as partition key
- **IAM Permissions:** User must have permission to access DynamoDB from your code
