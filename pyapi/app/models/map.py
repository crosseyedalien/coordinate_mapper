import psycopg2
from settings import db as pgconn
import pandas as pd
import logging as pylog
from pydantic import BaseModel


class MapType(BaseModel):
    # id: int
    title: str
    description: str
    created: str
    last_update: str


class Map:

    def get_all(self):
        sql_command = "SELECT id, title, description FROM map"
        return pgconn.query(sql_command, [])

    def get_map_coordinates(self, map_id):
        sql_command = "SELECT * FROM coordinates WHERE map_id = %s"
        return pgconn.query(sql_command, [map_id])

    def create_map(self, map_data: MapType):
        sql_command = """INSERT INTO map (title, description, created, last_update) VALUES (%s,%s,%s,%s) RETURNING *;"""
        result = pgconn.mutate(sql_command,
                               [map_data.title, map_data.description, map_data.created, map_data.last_update])
        return result

