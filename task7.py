"""
TASK 7: DICTIONARIES AND FOR-LOOPS

In this task you will learn to write for-loops for dictionaries.

A for-loop for a dictionary is very similar to a for-loop for a list. However, when looping through a dictionary there are two things we can loop through: keys and values.

We use the dictionary from task 7 as an example:

  amounts = {"Cheese": 17, "Chocolate": 25, "Banana": 10}

Before we start using for-loops, we will learn to list all values or keys from a dictionary. Here are some examples:

  keys = amounts.keys()
  values = amounts.values()

.keys() will list all keys in the dictionary and .values() will list all values. If you print the variables above it will look like this:

  ["Cheese", "Chocolate", "Banana"]
  ["17, 25, 10"]

You will end up with a list of items, and we have already learned how to loop though these!

  for key in keys:
    print(key)

  for value in values:
    print(value)

You can also use .keys() and .values() directly in the for-loop:

  for key in amounts.keys():
    print(key)

  for value in amounts.values():
    print(value)

This will give the same result as above without needing to write it to a variable. 

"""
amounts = {"Cheese": 17, "Chocolate": 25, "Banana": 10}

# A: Print all keys in the amounts dictionary.
# B: Print all values in the amounts dictionary.
# C: Make a for-loop that loops through all keys in the dictionary, and prints the corresponding values. Hint: Remember that you can use amounts[key] to get the corresponding value.

"""
You are now going to do an operation on the entire dictionary. In this example we have received 10 items extra of each product, and will update the dictionary by adding 10 to all amounts.  

We use a for loop to loop though all the keys and update all values.

for key in amounts.keys():
  amounts[key] = amounts[key] + 10

This is a shorter way to get the same result:
for key in amounts.keys():
  amounts[key] += 10

"""

# D: Someone orders 1 of each product in amounts. Subtract 1 on all the values in the dictionary.

# E: There is a restock at the fulfillment center. Add 20 to each product in the dictionary.

# -------------------------- Optional tasks -----------------------------------

"""
It is possible to loop through both keys and values in the same for-loop. You do it like this:

  for key, value in amounts.items():
    print("Key:", key)
    print("Value:", value)
"""

# F: Print keys and values in the amount dictionary like in the example above.

# G: Loop though keys and values in amounts. Print the key if the amount is bigger than 30.

# H: If you have made it to this task, nice work! Try to find out how to double the amount of all products where the length of the product name is bigger than 8 letters.

"""
Hint: As a software developer you will quickly get used to using google while programming. To find out how to find the length of a word, you can for example try to google "python length of variable".
"""
