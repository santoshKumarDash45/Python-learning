# For Loop - demonstrates iterating over a list with a conditional check

cart = [10, 20, 30, 40, 500, 600]   # list of cart items with prices

for item in cart:                   # iterate over each item in the cart list
    if item > 200:                  # check if the item price exceeds 200
        print("It requires insurnace to process the order", item)  # print warning for high-value item
        
    print("Processed items", item)  # always prints for every item regardless of the condition above



# output

# Processed items 10
# Processed items 20
# Processed items 30
# Processed items 40
# It requires insurnace to process the order 500
# Processed items 500
# It requires insurnace to process the order 600
# Processed items 600
