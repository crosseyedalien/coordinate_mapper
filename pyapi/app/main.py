from fastapi import FastAPI
from starlette.responses import JSONResponse
import psycopg2
import pandas as pd
from models import map

app = FastAPI()

# TODO: This should become an environment variable in docker-compose.yml
conn_string = "host=limspg port=5432 dbname=lims user=lims password=lims"

headers = {
    "content/type": "application/json",
}


@app.get("/")
def read_root():
    info = {
        "Hello": "Server is running"
    }

    return JSONResponse(content=info, headers=headers)


@app.get("/map")
def get_map_data():
    map_obj = map.Map()
    return JSONResponse(content=map_obj.get_all_in_dict(), headers=headers)


@app.get("/map/{map_id}")
def get_map_coordinates(map_id: int):
    conn = psycopg2.connect(conn_string)
    sql_command = "SELECT * FROM coordinates WHERE map_id = {}".format(map_id)
    data = pd.read_sql(sql_command, conn)
    data_dict = data.to_dict()
    return JSONResponse(content=data_dict, headers=headers)
