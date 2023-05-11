import psycopg2
import psycopg2.extras

DB_URL = 'dbname=dnd_app_db'
def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL) # This opens a connection
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # Cursor is used to run SQL commands
    cursor.execute(query, parameters) # This begins the transaction
    results = cursor.fetchall()
    connection.commit() # This ends the transaction
    connection.close() # This closes the connection
    return results