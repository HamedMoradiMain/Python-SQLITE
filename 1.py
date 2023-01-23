import sqlite3
conn = sqlite3.connect('customer.db')
# Create a cursor
cur = conn.cursor()
# Create a Table
cur.execute("""CREATE TABLE customers (
    first_name text, 
    last_name text,
    email text)""")
# Now for making changes on our database we need to commit it to our 
# database 
# Commit our command 
conn.commit()
# Close our connection
conn.close()
# Datatypes:
# NULL
# INTEGER 
# REAL 
# TEXT 
# BLOB