#Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Take user input for the list of numbers
input_str = input("Enter numbers separated by spaces: ")
user_list = list(map(int, input_str.split()))

print("Original List:", user_list)

# Apply bubble sort
bubble_sort(user_list)

print("Sorted List:", user_list)
