# Code Challenge Restaurants
This is a simple Restaurant Management System implemented in Python, utilizing SQLite for database management. The system consists of classes for Restaurants, Customers, and Reviews, each with their respective functionalities.

## Files
1. `restaurant.py`: Contains the implementation of the Restaurant, Customer, and Review classes.
2. `main.py`: Executes test functions to validate the methods defined in the Restaurant and Customer classes.
3. `db_setup.py`: Sets up the SQLite database schema by creating tables for restaurants, customers, and reviews.
4. `restaurant.db`: SQLite database file to store restaurant, customer, and review data.

## Implementation Details
<b>Restaurant Class:</b> Represents a restaurant with attributes such as ID, name, and price. It includes methods to fetch reviews for the restaurant, fetch customers who reviewed the restaurant, find the fanciest restaurant, and more.

<b>Customer Class:</b> Represents a customer with attributes such as ID, first name, and last name. It includes methods to fetch reviews by the customer, fetch restaurants visited by the customer, find the favorite restaurant of the customer, add a review for a restaurant, delete reviews by a customer for a restaurant, and more.

<b>Review Class:</b> Represents a review given by a customer for a restaurant. It includes methods to retrieve customer details for a review, restaurant details for a review, get the full review details, and provide a string representation of the review object.

## Usage
To use the Restaurant Management System:

1. Ensure you have Python installed on your system.
2. Run `db_setup.py` to set up the SQLite database schema.
3. Execute `main.py` to test the functionality of the Restaurant and Customer classes.

### Sample Output
```
Testing Restaurant Methods:

Reviews for restaurant_a:
Review for Java by Brian Kipkirui: ⭐⭐⭐⭐⭐ stars.

Customers of restaurant_a:
Customer ID: 1 Name: Brian Kipkirui

Testing Customer Methods:

Reviews by Brian:
Review for Java by Brian Kipkirui: ⭐⭐⭐⭐⭐ stars.

Restaurants visited by Brian:
Restaurant ID: 1, Name: Java, Price: 3

Brian's favorite restaurant:
Restaurant ID: 1, Name: Java, Price: 3

```

## License
This project is licensed under the MIT License - see the <a href = "https://github.com/bryokn/Code_Challenge_Restaurants/blob/main/LICENSE">LICENSE</a> file for details.

## Author
This code is written and maintained by Brian Kipkirui. You can contact me at <a href = "mailto:bryokn@gmail.com">bryokn@gmail.com.</a>
