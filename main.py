import sqlite3
from restaurant import Restaurant, Customer, Review

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO restaurants (name, price) VALUES (?, ?)', ('Java', 3))
cursor.execute('INSERT INTO restaurants (name, price) VALUES (?, ?)', ('Chicken Hut', 4))
cursor.execute('INSERT INTO restaurants (name, price) VALUES (?, ?)', ('Arbergine', 2))

cursor.execute('INSERT INTO customers (first_name, last_name) VALUES (?, ?)', ('Brian', 'Kipkirui'))
cursor.execute('INSERT INTO customers (first_name, last_name) VALUES (?, ?)', ('Joan', 'Bett'))
cursor.execute('INSERT INTO customers (first_name, last_name) VALUES (?, ?)', ('You', 'Guy'))

cursor.execute('INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (1 ,1, 5))
cursor.execute('INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (2, 2, 4))
cursor.execute('INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (3, 3, 4))

def test_restaurant_methods():
    restaurant_a = Restaurant(1, "Java", 3)
    print(restaurant_a.reviews(cursor))
    print(restaurant_a.customers(cursor))

def test_customer_methods():
    brian = Customer(1, "Brian", "Kipkirui")
    print(brian.reviews(cursor))
    print(brian.restaurants(cursor))
    print(brian.favorite_restaurant(cursor))

if __name__=="__main__":
    print("Testing Restaurant Methods:")
    test_restaurant_methods()
    print("\nTesting Customer Methods:")
    test_customer_methods()