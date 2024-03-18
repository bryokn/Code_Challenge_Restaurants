import sqlite3
from restaurant import Restaurant, Customer, Review
import db_setup

#connect to sqlite database
conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

#input data if not already existing
cursor.execute('INSERT OR IGNORE INTO restaurants (name, price) VALUES (?, ?)', ('Java', 3))
cursor.execute('INSERT OR IGNORE INTO restaurants (name, price) VALUES (?, ?)', ('Chicken Hut', 4))
cursor.execute('INSERT OR IGNORE INTO restaurants (name, price) VALUES (?, ?)', ('Arbergine', 2))

cursor.execute('INSERT OR IGNORE INTO customers (first_name, last_name) VALUES (?, ?)', ('Brian', 'Kipkirui'))
cursor.execute('INSERT OR IGNORE INTO customers (first_name, last_name) VALUES (?, ?)', ('Joan', 'Bett'))
cursor.execute('INSERT OR IGNORE INTO customers (first_name, last_name) VALUES (?, ?)', ('You', 'Guy'))

cursor.execute('INSERT OR IGNORE INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (1 ,1, '⭐⭐⭐⭐⭐'))
cursor.execute('INSERT OR IGNORE INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (2, 2, '⭐⭐⭐⭐'))
cursor.execute('INSERT OR IGNORE INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', (3, 3, '⭐⭐⭐⭐'))

conn.commit()

#test restaurant methods
def test_restaurant_methods():
    restaurant_a = Restaurant(1, "Java", 2)
    print("\nReviews for restaurant_a:")
    reviews_count = 0 #limit reviews to 3 per restaurant
    for review in restaurant_a.reviews(cursor):
        if reviews_count < 3:
            print(review.full_review(cursor))
            reviews_count += 1
        
    print("\nCustomers of restaurant_a:")
    for customer in restaurant_a.customers(cursor):
        print(customer)

#test customer methods
def test_customer_methods():
    brian = Customer(1, "Brian ", "Kipkirui")
    print("\nReviews by Brian:")
    reviews_count = 0 #limit reviews to 3 per customer
    for review in brian.reviews(cursor):
        if reviews_count < 3:
            print(review.__str__(cursor))
            reviews_count += 1
    
    print("\nRestaurants visited by Brian:")
    visited_restaurants = set()
    for restaurant in brian.restaurants(cursor):
        if restaurant.id not in visited_restaurants:
            print(restaurant)
            visited_restaurants.add(restaurant.id)
    
    print("\nBrian's favorite restaurant:")
    print(brian.favorite_restaurant(cursor))
    
    joan = Customer(2, "Joan ", "Bett")
    print("\nReviews by Joan:")
    reviews_count = 0
    for review in joan.reviews(cursor):
        if reviews_count < 3:
            print(review.__str__(cursor))
            reviews_count += 1
    
    print("\nRestaurants visited by Joan:")
    visited_restaurants = set()
    for restaurant in joan.restaurants(cursor):
        if restaurant.id not in visited_restaurants:
            print(restaurant)
            visited_restaurants.add(restaurant.id)
    
    print("\nJoan's favorite restaurant:")
    print(joan.favorite_restaurant(cursor))

#execute tests
if __name__=="__main__":
    print("Testing Restaurant Methods:")
    test_restaurant_methods()
    print("\nTesting Customer Methods:")
    test_customer_methods()

#close db connection
conn.close()