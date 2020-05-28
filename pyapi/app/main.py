from fastapi import FastAPI
from starlette.responses import JSONResponse
import psycopg2
import pandas as pd
from settings import logs
import logging
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
    logging.debug("*****************\nClient query root\n***************")
    return JSONResponse(content=info, headers=headers)


@app.get("/map")
def get_map_data():
    map_obj = map.Map()
    return JSONResponse(content=map_obj.get_all(), headers=headers)


@app.get("/map/{map_id}")
def get_map_coordinates(map_id: int):
    map_obj = map.Map()
    coordinates = map_obj.get_map_coordinates(map_id)
    return JSONResponse(content=coordinates, headers=headers)


@app.post("/map/add")
def create_new_map(new_map: map.MapType):
    map_obj = map.Map()
    result = map_obj.create_map(new_map)
    logging.debug("Result from create_map: {}".format(result))
    response = {"title": result["title"], "description": result["description"]}
    return JSONResponse(content=response, headers=headers)
