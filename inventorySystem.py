

import sqlite3


conn = sqlite3.connect('inventory.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS inventory
             (item TEXT, quantity INTEGER, price REAL)''')


c.execute("INSERT INTO inventory VALUES ('Widget', 10, 99.99)")
conn.commit()


c.execute("SELECT * FROM inventory")
items = c.fetchall()

for item in items:
    print(item)

conn.close()
