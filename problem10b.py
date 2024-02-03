import matplotlib.pyplot as plt

# Election results
parties = ['ABC', 'XYZ', 'MNP']
seats = [180, 200, 400 - (180 + 200)]

# Plotting the bar chart
plt.bar(parties, seats, color=['blue', 'green', 'red'])
plt.xlabel('Parties')
plt.ylabel('Number of Seats')
plt.title('Election Results - Year 2000')
plt.show()
