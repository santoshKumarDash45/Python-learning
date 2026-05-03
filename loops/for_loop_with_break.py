# For Loop with Break - demonstrates stopping a loop early using the break statement

cart = [10, 20, 300, 400, 500, 50, 60]  # list of cart items with prices

for item in cart:                        # iterate over each item in the cart list
    if item > 200:                       # check if the item price exceeds 200
        print("Unable to process the item due to insurance policy", item)  # print reason for stopping
        break                            # exit the loop immediately, remaining items are not processed

    print("Processed item", item)        # only prints if item is <= 200 (skipped once break is hit)




#output

# Processed item 10
# Processed item 20
# Unable to process the item due to insurance policy 300
