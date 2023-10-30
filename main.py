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


class vm_get_projects(BaseModel):
    name: str
    lead_name: str
    count_user: int
    is_finish: bool


cursor = connect.cursor()

app = FastAPI()


@app.get('/')
def hello():
    return "Донт ворри, еверитхинк ворк!!!!!"


# uvicorn main:app --reload

@app.get('/get_project')
def get_proj():
    cursor.execute("""
    SELECT name, lead_name, count_user, is_finish from languages;
    """)
    result = cursor.fetchall()
    list_proj = []
    for proj in result:
        list_proj.append(vm_get_projects(
            name=proj[0],
            lead_name=proj[1],
            count_user=proj[2],
            is_finish=proj[3]
        ))

    return {"projects": list_proj}
