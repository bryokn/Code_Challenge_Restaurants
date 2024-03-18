import sqlite3
class Restaurant:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
   
   #method to fetch reviews for a restaurant 
    def reviews(self, cursor):
        cursor.execute('SELECT DISTINCT * FROM reviews WHERE restaurant_id = ?', (self.id,))
        reviews_data = cursor.fetchall()
        return [Review(review_data[0], review_data[1], review_data[2]) for review_data in reviews_data]
    
    #method to fetch customers who reviewed a restaurant
    def customers(self, cursor):
        cursor.execute('''
                       SELECT DISTINCT customers.id, customers.first_name, customers.last_name 
                       FROM customers JOIN reviews ON customers.id = reviews.customer_id 
                       WHERE reviews.restaurant_id = ?
                       ''',(self.id,))
        customers_data = cursor.fetchall()
        return [Customer(customer_data[0], customer_data[1], customer_data[2]) for customer_data in customers_data]
    
    #class method to find the fanciest restaurant
    @classmethod
    def fanciest(cls, cursor):
        cursor.execute('SELECT DISTINCT * FROM restaurants ORDER BY price DESC LIMIT 1')
        fanciest_data = cursor.fetchone()
        if fanciest_data:
            return cls (*fanciest_data)
    
    #string representation of restaurant object
    def __str__(self):
        return f"Restaurant ID: {self.id}, Name: {self.name}, Price: {self.price}" 

class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    #fetch reviews by a customer        
    def reviews(self, cursor):
        cursor.execute('SELECT DISTINCT * FROM reviews WHERE customer_id = ?', (self.id,))
        reviews_data = cursor.fetchall()
        return [Review(review_data[0], review_data[1], review_data[2]) for review_data in reviews_data]
    
    #fetch restaurants visited by a customer    
    def restaurants(self, cursor):
        cursor.execute('''
                        SELECT DISTINCT restaurants.* FROM restaurants JOIN reviews ON restaurants.id = reviews.restaurant_id 
                        WHERE reviews.customer_id = ?''', (self.id,))
        restaurants_data = cursor.fetchall()
        #print("Printing restaurant data: ")
        print(restaurants_data)
        return [Restaurant(restaurant_data[0], restaurant_data[1], restaurant_data[2]) for restaurant_data in restaurants_data]
    
    #get full name of the customer        
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    
    #find the favorite restaurant of a customer    
    def favorite_restaurant(self, cursor):
        cursor.execute('''
                        SELECT restaurants.*, MAX(reviews.star_rating) AS max_rating FROM restaurants JOIN reviews 
                        ON restaurants.id = reviews.restaurant_id WHERE reviews.customer_id = ? GROUP BY restaurants.id
                        ORDER BY max_rating DESC LIMIT 1''', (self.id,))
        favorite_data = cursor.fetchone()
        if favorite_data:
            return Restaurant(favorite_data[0], favorite_data[1], favorite_data[2])
    
    #Add a review for a restaurant by a customer        
    def add_review(self, restaurant, rating, cursor, conn):
        cursor.execute('SELECT DISTINCT * FROM reviews WHERE restaurant_id = ? AND customer_id = ?', (restaurant.id, self.id))
        existing_review = cursor.fetchone()
        if existing_review:
            print("Review already exists.")
            return
        
        cursor.execute('''
                        INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)''', (restaurant.id, self.id, rating))
        conn.commit()
    
    #string representation of customer object
    def __str__(self):
        return f"Customer ID: {self.id} Name: {self.first_name} {self.last_name}"
    
   #delete reviews by a customer for a restaurant        
    def delete_reviews(self, restaurant, cursor, conn):
        cursor.execute('''
                        DELETE FROM reviews WHERE restaurant_id = ? AND customer_id = ?''', (restaurant.id, self.id))
        conn.commit()
        
class Review:
    def __init__(self, restaurant_id, customer_id, star_rating):
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating
    
    #get customer details for a review    
    def customer(self, cursor):
        cursor.execute('SELECT DISTINCT * FROM customers WHERE id = ?', (self.customer_id,))
        customer_data = cursor.fetchone()
        if customer_data:
            return Customer(*customer_data)
    
    #get restaurant details for a review
    def restaurant(self, cursor):
        cursor.execute('SELECT DISTINCT * FROM restaurants WHERE id = ?', (self.restaurant_id,))
        restaurant_data = cursor.fetchone()
        if restaurant_data:
            return Restaurant(*restaurant_data)
    
    #get full review details
    def full_review(self, cursor):
        customer = self.customer(cursor)
        restaurant = self.restaurant(cursor)
        if customer and restaurant:
            return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."
    
    #string representation of Review object
    def __str__(self, cursor):
        review_details = self.full_review(cursor)
        if review_details:
            return review_details
        else:
            return f"Review ID: {self.id} Restaurant ID: {self.restaurant_id}, Customer ID: {self.customer_id}, Rating: {self.star_rating}"