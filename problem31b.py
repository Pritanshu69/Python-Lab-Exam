result_list = []

for i in range(1, 27):
    letter = chr(ord('a') + i - 1)
    result_list.append(letter * i)

print(result_list)
