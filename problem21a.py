input_list = input("Enter a list of numbers by giving spaces").split()
new_list = [int(num) for num in input_list]

result_list = [num for num in new_list if num == sum(int(digit)**3 for digit in str(num))]

print("Numbers where the sum of cubes of digits is equal to the number: ", result_list)

if result_list:
    largest = max(result_list)
    print("\nLargest Number:",largest)
    smallest = min(result_list)
    print("Smallest Number:",smallest)
else:
    print("No such number found")