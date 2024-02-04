# Get user input for the total number of cookies, box capacity, and container capacity
total_cookies = int(input("Enter the total number of cookies: "))
box_capacity = int(input("Enter the capacity of a box (number of cookies per box): "))
container_capacity = int(input("Enter the capacity of a container (number of boxes per container): "))

# Calculate the number of boxes and containers needed
num_boxes = total_cookies // box_capacity
num_containers = num_boxes // container_capacity

# Calculate leftover cookies and boxes
leftover_cookies = total_cookies % box_capacity
leftover_boxes = num_boxes % container_capacity

# Output the results
print("\nNumber of boxes needed:", num_boxes)
print("Number of containers needed:", num_containers)
print("Leftover cookies:", leftover_cookies)
print("Leftover boxes:", leftover_boxes)
