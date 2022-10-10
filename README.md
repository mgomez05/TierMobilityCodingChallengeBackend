# Coding Challenge Submission

Hello to those viewing this repository. This repository aims to help solve the [Tier Mobility Coding Challenge](https://github.com/TierMobility/frontend-challenge/tree/feat/fullstack-challange#coding-challenge-)

This code goes hand in hand with the frontend developed for completing the challenge. Please start running this backend first, and then run the [frontend](https://github.com/mgomez05/TierMobilityCodingChallenge) on the same machine to make sure the web app runs correctly.

To start up the server, head to the section **Getting Started**

To see the available endpoints provided by this server, head to the section **API**

## Getting Started 

Below are the steps necessary to get the backend up and running on a new machine:

### Step 0: Clone the repository

### Step 1: Install Postgres

- For Mac, install it using Homebrew: https://wiki.postgresql.org/wiki/Homebrew
- For Windows, download the Postgres installer for Windows: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
   - Run the installer, and type AND REMEMBER a password for Postgres when prompted by the installer
   - Update your Environment Variable PATH by adding the location of your postgres executable to PATH (i.e. `C:\Program Files\PostgreSQL\11\bin` )

### Step 2: Create the Postgres database and database user

0. Open postgres on the command line by typng `psql -U postgres`, and enter the password you entered during installation
1. Create the database for the django project: `CREATE DATABASE tierdb;`
2. Create the database user for the django project: `CREATE USER tieruser WITH PASSWORD 'tier';`
3. Grant the database user all privileges: `GRANT ALL PRIVILEGES ON DATABASE tierdb TO tieruser;`

Once the database is setup ... 

## Step 3: Create a Virtual Environment  

1. `virtualenv -p python3 env`
2. Mac: `source env/bin/activate`
   Windows: `source env/Scripts/activate`
   
Once the virtual environment is activated.... 

## Step 4: Install Dependencies

1. `pip install -r requirements.txt `

## Step 5: Migrate Tables and Run Server

From the same directory as `manage.py`, run: 

1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver`

This will start the server at localhost:8000 

## API

### Get a Shortened URL
POST `api/shortURl`
- Required Fields
    - `realUrl`
- Response: 
    - Success
        - HTTP Status : 200
        - Payload (JSON)
            - `shortUrl` corresponding to the `realUrl` provided in the request

### Get the Original URL from a Shortened Url
GET `api/shortURl`
- Required Fields
    - `shortUrl`
- Response: 
    - Success
        - HTTP Status : 200
        - Payload (JSON)
            - `realUrl`, which is the original url used to generate `shortUrl` provided in the request