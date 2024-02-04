input_seq = input("Enter the string using hyphens: ")

words = input_seq.split('-')

sorted_words = sorted(words)

output_seq = end = '-'.join(sorted_words)

print(f"The sorted sequence is: {output_seq}")