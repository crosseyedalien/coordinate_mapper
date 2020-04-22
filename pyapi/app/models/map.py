import psycopg2
from settings import db as pgconn
import pandas as pd
import logging as pylog
from . import base_model


class Map(base_model.BaseModel):

    def get_all_in_dict(self):
        conn = psycopg2.connect(pgconn.conn_string)
        sql_command = "SELECT id, title, description FROM map"
        data = pd.read_sql(sql_command, conn)
        return data.to_dict()

    def get_all_for_graphql(self):
        data_dict = self.get_all_in_dict()
        return self.place_all_records_in_list(data_dict)

    def place_all_records_in_list(self, pandas_dict):
        all_dirs = []
        # determine number of DB records this dictionary represents
        rec_num = len(pandas_dict["title"])
        pylog.debug("Found {} records in directory file.".format(rec_num))

        # iterate over all the records
        for i in range(rec_num):
            pylog.debug("Working with directory #{}, '{}'...".format(i, pandas_dict["title"][i]))
            all_dirs.append(self.create_record_dict(pandas_dict, i))

        pylog.debug("All directories: {}".format(all_dirs))
        return all_dirs

    def create_record_dict(self, pandas_dict, index=0):
        if len(pandas_dict) != 29:
            return {}

        new_dict = {
            "title": pandas_dict["title"][index],
            "description": pandas_dict["description"][index],
            "created": pandas_dict["created"][index],
            "last_updated": pandas_dict["last_updated"][index],
        }
        return new_dict
