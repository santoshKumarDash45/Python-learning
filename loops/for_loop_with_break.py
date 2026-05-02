# For Loop with Break - demonstrates stopping a loop early using the break statement

cart = [10, 20, 300, 400, 500, 50, 60]

for item in cart:
    if item > 200:
        print("Unable to process the item due to insurance policy", item)
        break

    print("Processed item", item)




#output

# Processed item 10
# Processed item 20
# Unable to process the item due to insurance policy 300