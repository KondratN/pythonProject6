from fastapi import FastAPI
import psycopg2 as psycopg
from dotenv import dotenv_values
from pydantic import BaseModel

config = dotenv_values(".env")

connect = psycopg.connect(
    host=config["HOST"],
    port=config["PORT"],
    database=config["DBNAME"],
    user=config["USERID"],
    password=config["USERPW"]
)

cursor = connect.cursor()

app = FastAPI()


@app.get('/')
def hello():
    return "Донт ворри, еверитхинк ворк!!!!!"

# uvicorn main:app --reload
