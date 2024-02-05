import matplotlib.pyplot as plt

# Election results
parties = ['X', 'Y', 'Z']
results = [45, 30, 25]  # Replace these values with actual results

# Plotting the bar graph
plt.bar(parties, results, color=['blue', 'green', 'red'])
plt.xlabel('Parties')
plt.ylabel('Seats')
plt.title('Election Results in West Bengal')
plt.show()
