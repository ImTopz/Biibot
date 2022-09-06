import sqlite3

class Sql:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
    def open(self, db):
        self.conn = sqlite3.connect(db)