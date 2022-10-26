import sqlite3

def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def query_db(query, args=(), one=False):
    conn = get_db_conn().execute(query, args)
    rv = conn.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv