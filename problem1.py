def remove_first_last_char(input_str):
    if len(input_str)>2:
        return input_str[1:-1]
    else:
        return "String size is smaller"
def combine_first_middle_and_last_chars(s1,s2):
    result = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]
    return result
def append_in_middle(s1,s2):
    midIdx=len(s1)//2
    result = s1[:midIdx]+ s2 + s1[midIdx:]
    return result

#take user input
string1 = input("Enter the first string: ")
string2 = input("Enter the secoond string: ")

result_i = remove_first_last_char(string1)
print(f"Task i: {result_i}")

result_ii = combine_first_middle_and_last_chars(string1,string2)
print(f"Task_ii: {result_ii}")

result_iii = append_in_middle(string1,string2)
print(f"Task_iii: {result_iii}")
