# You have a football field that is 92 meter long and 48.8 meter wide.
# Find out total area using python and print it.
length = 92
width = 48.8
area_of_field = length*width
print(f"Area of the football field is {area_of_field}")

# You bought 9 packets of potato chips from a store.
# Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?
number_of_packets_bought = 9
cost_per_packet = 1.49
total_cost = number_of_packets_bought*cost_per_packet
cash_given = 20
cash_back = cash_given - total_cost
print(f"Total change to be remitted: {cash_back}")

# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
length_of_tile = 5.5
cost_per_sq_ft = 500
area_of_square = length_of_tile**2
total_cost_of_replacement = area_of_square*cost_per_sq_ft
print(f"Total cost of replacement: Rs.{total_cost_of_replacement}")


# Print binary representation of number 17
print(f"Binary Representation of 17 is {format(17,"b")}")