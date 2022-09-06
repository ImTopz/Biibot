#!/usr/bin/env python3 
from flask import Flask
import click

app = Flask(__name__)
@app.route('/')
def root():
   return "Hello World"

@click.command()
@click.option('--host', default='localhost', help='set hostname to listen on')
@click.option('--port', default=5000, help='set service port')
@click.option('--db', default="data.db", help='set sqlite3 db path')

def main(host, port, db):
    """Accounting bot based on gocq-http and flask"""
    api=Api(db)
    app.run(host, port)

if __name__ == '__main__':
    main()