from sql import Sql

class Api:
    def __init__(self,db):
        self.sql = Sql(db)
