### TODO:
#    - import the Shirt class from the shirt.py file
###

from shirt_class import Shirt 


### TODO:
#    - insantiate a shirt object with the following characteristics:
#        - color red, size S, style long-sleeve, and price 25
#    - store the object in a variable called shirt_one
#
#
###

shirt_one = Shirt('red', 'S', 'long-sleeve', 23)

#Testing shirt_one initialization
print(shirt_one.color)
print(shirt_one.size)
print(shirt_one.style)
print(shirt_one.price)

### TODO:
#     - print the price of the shirt using the price attribute
#     - use the change_price method to change the price of the shirt to 10
#     - print the price of the shirt using the price attribute
#     - use the discount method to print the price of the shirt with a 12% discount
#
###

print('Before Sale:',shirt_one.price)
shirt_one.change_price(10)
print('After Sale:',shirt_one.price)
print('With Discount:',shirt_one.discount(0.12))

### TODO:
#
#    - instantiate another object with the following characteristics:
# .       - color orange, size L, style short-sleeve, and price 10
#    - store the object in a variable called shirt_two
#
###
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

#Testing shirt_two initialization
print(shirt_two.color)
print(shirt_two.size)
print(shirt_two.style)
print(shirt_two.price)

### TODO:
#
#    - calculate the total cost of shirt_one and shirt_two
#    - store the results in a variable called total
#    
###

total = shirt_one.price + shirt_two.price

print (total)

### TODO:
#
#    - use the shirt discount method to calculate the total cost if
#       shirt_one has a discount of 14% and shirt_two has a discount
#       of 6%
#    - store the results in a variable called total_discount
###

total_discount = shirt_one.discount(0.14) + shirt_one.discount(0.06)
print (total_discount)

