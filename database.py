from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv() #loads the .env file and its variables

DATABASE_URL = os.getenv("DATABASE_URL") #pure read, assigns the actual value to database url

engine = create_engine(DATABASE_URL) #creates an instance of the engine that knows how to read sql

if __name__ == "__main__":
    with engine.connect() as connection:
        print("Connected to the database!")