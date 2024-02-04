# Get user input for principal amount, rate of interest, and time
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time period (in years): "))

# Calculate amount payable after simple interest
simple_interest = (principal_amount * rate_of_interest * time) / 100
amount_after_simple_interest = principal_amount + simple_interest

# Calculate amount payable after compound interest
compound_interest = principal_amount * ((1 + rate_of_interest / 100) ** time - 1)
amount_after_compound_interest = principal_amount + compound_interest

# Print the results
print(f"\nAmount payable after Simple Interest: {amount_after_simple_interest}")
print(f"Amount payable after Compound Interest: {amount_after_compound_interest}")
