import json
from lib2to3.pgen2.pgen import DFAState
import os
import psycopg2
from largePayload import getLargePayload
from mediumPayload import getMediumPayload

from smallPayload import getSmallPayload


conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS payload;')
cur.execute('CREATE TABLE payload (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'data json NOT NULL);'
                                 )

# Insert data into the table
cur.execute("""
            INSERT INTO payload (title, data)
            VALUES (%s, %s);
            """,
            ('small', json.dumps(getSmallPayload())))

# Insert data into the table
cur.execute("""
            INSERT INTO payload (title, data)
            VALUES (%s, %s);
            """,
            ('medium', json.dumps(getMediumPayload())))# Insert data into the table
cur.execute("""
            INSERT INTO payload (title, data)
            VALUES (%s, %s);
            """,
            ('large', json.dumps(getLargePayload())))


# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('Anna Karenina',
#              'Leo Tolstoy',
#              864,
#              'Another great classic!')
#             )

conn.commit()

cur.close()
conn.close()