input_str1 = input("Enter the first list: ")
list1 = list(map(int,input_str1.split()))
input_str2 = input("Enter the second list: ")
list2 = list(map(int,input_str2.split()))

union_list = list(set(list1) | set(list2))
print(f"union of the list: {union_list}")
instersection_list = list(set(list1) & set(list2))
print(f"intersection of the list: {instersection_list}")