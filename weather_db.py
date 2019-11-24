import sqlite3

# create weather database

# conn = sqlite3.connect('weather.db')
# print('create database successfully')
# conn.execute('create table cities(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)')
# print('created table successfully')
# conn.close()

# insert data into database

# city = 'Surat'
# with sqlite3.connect('weather.db') as conn:
#     cur = conn.cursor()
#     cur.execute("INSERT into cities (name) values (?)", (city,))
#     conn.commit()
#     print("City Is Successfully Added")


# fetch data from the database.

city_list = []

con = sqlite3.connect('weather.db')
cur = con.cursor()
cur.execute("select DISTINCT name from cities ORDER BY id DESC LIMIT 3")
rows = cur.fetchall()
for row in rows:
    for name in row:
        city_list.append(name)    
con.close()

print(city_list)