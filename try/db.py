#!/usr/bin/python3
import sqlite3 as sql

# Connect to database
koneksi = sql.connect('exam.db')

# Create kursor
kursor = koneksi.cursor()

# Create Table
kursor.execute('''
               CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY,
                   userName TEXT,
                   email TEXT
               )
    ''')

# INPUT DATA TO DATABASE
kursor.execute("INSERT INTO user (userName, email) VALUES (?, ?)", ('Udin','Udin@yahho.com'))

# chang commit
koneksi.commit()

# query Data
kursor.execute("SELECT * FROM user")
rows = kursor.fetchall()

for row in rows:
    print(row)
    
# close connetion
koneksi.close()
