from sqlalchemy import create_engine

from config.main import *

class DatabaseManager():

    def initDB(*args, **kwargs):
        print('Connecting to database...')
        db = create_engine(DB_URL)
        return db
