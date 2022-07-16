
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from largePayload import *
from mediumPayload import *
from smallPayload import *
import os
import psycopg2
# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/small-json-payload')
def small_payload():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM payload;')
    payload = cur.fetchall()
    cur.close()
    conn.close()
    return render_template(payload=payload)

@app.route('/medium-json-payload')
def medium_payload():
    return getMediumPayload()

@app.route('/large-json-payload')
def large_payload():
    return getLargePayload()
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)