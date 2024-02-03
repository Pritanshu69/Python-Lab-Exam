import re
# Take user input
input_string = input("Enter a string: ")

# Perform a case-insensitive search for "India" using re module

occurrences = [match.start() for match in re.finditer('India',input_string,re.IGNORECASE)]

# Print the positions of occurrences
if occurrences:
    print(f'Occurrences of "India" (case-insensitive) at positions: {occurrences}')
else:
    print('No occurrences found.')
