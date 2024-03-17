import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS restaurants (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   price INTEGER
               )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS reviews(
                   id INTEGER PRIMARY KEY,
                   restaurant_id INTEGER,
                   customer_id INTEGER,
                   star_rating INTEGER,
                   FOREIGN KEY (restaurant_id) REFERENCES restaurants (id),
                   FOREIGN KEY (customer_id) REFERENCES customers (id)
               )
               ''')

conn.commit()