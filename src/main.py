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

def main(host, port):
    """Accounting bot based on gocq-http and flask"""
    app.run(host, port)

if __name__ == '__main__':
    main()