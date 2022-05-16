"""
TASK 6: DICTIONARIES

In this task you will learn about a datatype called dictionary.

Example of a dictionary:

  customer = {"name": "Oda", "city": "Oslo"}
  
Everything between the curly brackets is a dictionary. In the example above, "name" and "city" is what we call keys, and "Oda" and "Oslo" is values.
Keys can be used to access a value, and it can be done like this:

  customer_name = customer["name"]

In this example customer["name"] will give the value that belongs to "name", and that value is "Oda" in this case. 

You can do the same for city:

  customer_city = customer["city"]

Here customer["city"] will return the value that belongs to "city", and the value in this case is "Oslo".

We have made two dictionaries that you will work on in this task. One contains information about a specific product, and the other gives and overview of the amount we have of different products. 

"""

product = {"name": "Cheese", "price": 50, "category": "Dairy"}

# A: Get the name of the product.

# B: Get the price of the product.

# C: Get the category of the product.

"""
Below you see an example of another dictionary. This dictionary contains many products and you can get the amount we have in the fulfillment center of each product. The key in this dictionary is the name of the product, and the amount is the value. 
"""


amounts = {"Cheese": 17, "Chocolate": 25, "Banana": 10}

# D: Get the amount of cheese we have in the fulfillment center.

# E: Get the amount of chocolate we have in the fulfillment center.

# F: Get the amount of bananas we have in the fulfillment center.

"""
You can change specific values in a dictionary. It is done like this:
amounts["Cheese"] = 16

The the amount of cheese if changed from 17 to 16.
"""

# G: We sell 3 chocolates. Change the amount of chocolates to match this.

# H: We sell out of bananas. Put the amount of bananas to 0.

"""
You can add new sets of keys and values to a dictionary the same way as you change the value, except that the key dont exists in the dictionary. For example, you can add apples to the dictionary like this:

amounts["Apple"] = 10
"""

# I: You work in the fulfillment center and get a delivery of 42 bottles of milk. Change the dictionary so that the milk is represented.

# J: We get a delivery of 20 broccoli. Add this to the dictionary and print the dictionary.


