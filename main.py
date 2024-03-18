import sqlite3
from restaurant import Restaurant, Customer, Review
import db_setup

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

cursor.execute('INSERT OR IGNORE INTO restaurants (name, price) VALUES (?, ?)', ('Java', 3))
cursor.execute('INSERT OR IGNORE INTO restaurants (name, price) VALUES (?, ?)', ('Chicken Hut', 4))
cursor.execute('INSERT OR IGNORE INTO restaurants (name, price) VALUES (?, ?)', ('Arbergine', 2))

cursor.execute('INSERT OR IGNORE INTO customers (first_name, last_name) VALUES (?, ?)', ('Brian', 'Kipkirui'))
cursor.execute('INSERT OR IGNORE INTO customers (first_name, last_name) VALUES (?, ?)', ('Joan', 'Bett'))
cursor.execute('INSERT OR IGNORE INTO customers (first_name, last_name) VALUES (?, ?)', ('You', 'Guy'))

cursor.execute('INSERT OR IGNORE INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (1 ,1, 5))
cursor.execute('INSERT OR IGNORE INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (2, 2, 4))
cursor.execute('INSERT OR IGNORE INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (3, 3, 4))

conn.commit()

def test_restaurant_methods():
    restaurant_a = Restaurant(1, "Java", 2)
    print("Reviews for restaurant_a:")
    for review in restaurant_a.reviews(cursor):
        print(review.full_review(cursor))
        
    print("Customers of restaurant_a:")
    for customer in restaurant_a.customers(cursor):
        print(customer)

def test_customer_methods():
    brian = Customer(1, "Brian ", "Kipkirui")
    print("Reviews by Brian:")
    for review in brian.reviews(cursor):
        print(review.__str__(cursor))
    
    print("Restaurants visited by Brian:")
    visited_restaurants = set()
    for restaurant in brian.restaurants(cursor):
        if restaurant.id not in visited_restaurants:
            print(restaurant)
            visited_restaurants.add(restaurant.id)
    
    print("Brian's favorite restaurant:")
    print(brian.favorite_restaurant(cursor))

if __name__=="__main__":
    print("Testing Restaurant Methods:")
    test_restaurant_methods()
    print("\nTesting Customer Methods:")
    test_customer_methods()

conn.close()