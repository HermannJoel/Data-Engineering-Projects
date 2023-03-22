import pandas as pd
import psycopg2
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine, Column
from sqlalchemy.types import Integer, String, Date, DECIMAL, Numeric
from sqlalchemy.orm import sessionmaker
import configparser
import os
import sys
import pymongo
from pymongo import MongoClient


sys.path.insert(0, 'D:/git-local-cwd/Data-Engineering-Projects/blx_mdp_data-eng/etls/functions/')
from etl_functions import ChooseCwd, QueryDataFromPostgreSQL, InsertDocToMongoDB 
ChooseCwd(cwd="D:/git-local-cwd/Data-Engineering-Projects/")
from queries.postgres_dw_queries import*

#Load Config
config_file=os.path.join(os.path.dirname("__file__"), 'Config/config.ini')
config=configparser.ConfigParser(allow_no_value=True)
config.read(config_file)

# Initialize Variables
postgres_conn_str=os.path.join(os.path.dirname("__file__"), config['develop']["postgres_conn_str"])
mongodbatlas_conn_str=os.path.join(os.path.dirname("__file__"), config['develop']["mongodbatlas_conn_str"])
mssql_conn_str=os.path.join(os.path.dirname("__file__"), config['develop']["mssql_conn_str"])


if __name__ == '__main__':
    InsertDocToMongoDB(dest_db="dw", dest_collection="ViewHedgeAsset", 
                       query_name=viewhedgeasset_query, mongodb_conn_str=mongodbatlas_conn_str, 
                       postgres_conn_str=postgres_conn_str, date_format='%Y-%m-%d'
                      )




