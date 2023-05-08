import string
# print(string.ascii_lowercase)

def is_pangram(sentence):
    all_lower = string.ascii_lowercase
    sentence_lower = sentence.lower()
    for char in all_lower:
        if char not in sentence_lower:
            return False
    return True
sentence = input("Insert your sentence: ")
pangram = is_pangram(sentence)
if pangram:
    print("Your sentence is pangram")
else:
    print("Your sentence is not a pangram")

def get_sentence() -> str:
    return input("Insert your sentence: ")

pangram = is_pangram(get_sentence())