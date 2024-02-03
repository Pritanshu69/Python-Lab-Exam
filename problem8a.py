digit = input("Enter the value digit from 0 to 9: ")
digit = int(digit)
digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
if 0<=digit<=9:
    print(f"{digit} is: {digit_words[digit]}")
else:
    print("Enter a valid number")
