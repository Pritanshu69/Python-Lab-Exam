# Get user input for consumption in units
consumption = int(input("Enter the consumption in units: "))

# Calculate the amount to be paid based on the specified rate structure
if consumption <= 200:
    rate_per_unit = 0.50
    total_amount = consumption * rate_per_unit
elif 201 <= consumption <= 400:
    rate_per_unit = 0.65
    total_amount = 100 + (consumption - 200) * rate_per_unit
elif 401 <= consumption <= 600:
    rate_per_unit = 0.80
    total_amount = 250 + (consumption - 400) * rate_per_unit
else:
    rate_per_unit = 1.25
    total_amount = 425 + (consumption - 600) * rate_per_unit

# Print the result
print(f"The amount to be paid for {consumption} units is Rs. {total_amount:.2f}")
