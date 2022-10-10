# Local Setup 

## Local Database 

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
