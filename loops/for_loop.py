# For Loop - demonstrates iterating over a list with a conditional check

cart = [10, 20 , 30 , 40 , 500, 600]

for item in cart:
    if item > 200:
        print("It requires insurnace to process the order", item)
        
    print("Processed items", item)



# output

# Processed items 10
# Processed items 20
# Processed items 30
# Processed items 40
# It requires insurnace to process the order 500
# Processed items 500
# It requires insurnace to process the order 600
# Processed items 600