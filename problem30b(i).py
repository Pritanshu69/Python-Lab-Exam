list1 = input("Enter the first list (comma-separated values): ").split(',')
list2 = input("Enter the second list (comma-separated values): ").split(',')

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

diff_idx = None

for i in range(len(list1)):
    if list1[i] != list2[i]:
        diff_idx = i
        break

if diff_idx is not None:
    print(f"The lists differ at index {diff_idx}.")
else:
    print("The lists are identical.")