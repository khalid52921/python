# Define variables for the prices of three items
item1_price = 50.0  
item2_price = 30.0  
item3_price = 20.0  

# Define the total budget
budget = 120.0  

# Calculate the total cost of the items
total_cost = item1_price + item2_price + item3_price

# Compare the total cost with the budget and calculate the difference
if total_cost <= budget:
    money_left = budget - total_cost
    print(f"Total cost is ${total_cost:.2f}.")
    print(f"You are within budget. You have ${money_left:.2f} left.")
else:
    money_needed = total_cost - budget
    print(f"Total cost is ${total_cost:.2f}.")
    print(f"You are over budget. You need an additional ${money_needed:.2f}.")
