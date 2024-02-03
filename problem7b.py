sample_list = input("Enter a list of numbers separated by spaces: ").split()

sample_list = [int(num) for num in sample_list]

unique_list = list(set(sample_list))

print("Original List:", sample_list)
print("Unique List:", unique_list)

#NOTE - not working in vs code but working in online compiler Lol XD Lmao WTF!
