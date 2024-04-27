from mysqlconnect import connect_db
from mysqlx import Schema, Session



database:Session = connect_db()



while database.is_open():

