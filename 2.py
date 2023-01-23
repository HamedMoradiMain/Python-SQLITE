import sqlite3
# Insert One Record Into The Table
conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute("INSERT INTO customers VALUES ('Qool','Morad','shah@dude.com')")
# Commit Changes 
conn.commit()
# Close Connection
conn.close()