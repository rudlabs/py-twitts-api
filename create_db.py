import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS twitter (hashtag text PRIMARY KEY, user text, followers int, posts int, location text, created text)"

creating_twetts = "INSERT INTO twitter VALUES ('#DevOps', 'James Gott', 1525, 32863, 'North East, England', '12 November 2019 - 01:26:44')"

cursor.execute(create_table)
cursor.execute(creating_twetts)

connection.commit()
connection.close()
