import sqlite3

#Connect to SQLITE database
conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

#create restaurants table if not existing
cursor.execute('''
               CREATE TABLE IF NOT EXISTS restaurants (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   price INTEGER
               )
               ''')
#create customers table if not existing
cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers (
                   id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT
               )
               ''')
#create reviews table if not existing
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
#commit changes to database
conn.commit()

#Close db connection