class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def reviews(self):
        cursor.execute('SELECT * FROM reviews WHERE restaurant_id = ?', (self.id,))
        reviews_data = cursor.fetchall()
        return [Review(*review_data) for review_data in reviews_data]
    
    def customers(self):
        cursor.execute('''
                       SELECT customers.* FROM customers JOIN reviews ON customers.id = reviews.customer_id 
                       WHERE reviews.restaurant_id = ?
                       ''',(self.id,))
        customers_data = cursor.fetchall()
        return [Customer(*customers_data) for customer_data in customers_data]
    
    @classmethod
    def fanciest(cls):
        cursor.execute('SELECT * FROM restaurants ORDER BY price DESC LIMIT 1')
        fanciest_data = cursor.fetchone()
        if fanciest_date:
            return cls (*fanciest_data)
        
class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
            
    def reviews(self):
        cursor.execute('SELECT * FROM reviews WHERE customer_id = ?', (self.id,))
        reviews_data = cursor.fetchall()
        return [Review(*review_data) for review_data in reviews_data]
        
    def restaurants(self):
        cursor.execute('''
                        SELECT restaurants.* FROM restaurants JOIN reviews ON restaurants.id = reviews.restaurant_id 
                        WHERE reviews.customer_id = ?''', (self.id,))
        restaurants_data = cursor.fetchall()
        return [Restaurant(*restaurant_data) for restaurant_data in restaurants_data]
        
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
        
    def favorite_restaurant(self):
        cursor.execute('''
                        SELECT restaurants.*, MAX(reviews.star_rating) AS max_rating FROM restaurants JOIN reviews 
                        ON restaurants.id = reviews.restaurant_id WHERE reviews.customer_id = ? GROUP BY restaurants.id
                        ORDER BY max_rating DESC LIMIT 1''', (self.id,))
        favorite_data = cursor.fetchone()
        if favorite_data:
            return Restaurant(*favorite_data)
            
    def add_review(self, restaurant, rating):
        cursor.execute('''
                        INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)''', (restaurant.id, self.id, rating))
        conn.commit()
        
    def delete_reviews(self, restaurant):
        cursor.execute('''
                        DELETE FROM reviews WHERE restaurant_id = ? AND customer_id = ?''', (restaurant.id, self.id))
        conn.commit()
        
class Review:
    def __init__(self, restaurant_id, customer_id, star_rating):
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating
        
    def customer(self):
        cursor.execute('SELECT * FROM customers WHERE id = ?', (self.customer_id,))
        customer_data = cursor.fetchone()
        if customer_data:
            return Customer(*customer_data)
    
    def restaurant(self):
        cursor.execute('SELECT * FROM restaurants WHERE id = ?', (self.restaurant_id))
        restaurant_data = cursor.fetchone()
        if restaurant_data:
            return Restaurant(*restaurant_data)
    
    def full_review(self):
        customer = self.customer()
        restaurant = self.restaurant()
        if customer and restaurant:
            return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."