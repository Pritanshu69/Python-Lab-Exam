input_sentence = input("Enter the sentence: ")

alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

sentence_set = set(input_sentence.lower())

if alphabet_set.issubset(sentence_set):
     print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")