# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def length_last_word(s):
    string = input("Enter a string: ")
    words = string.strip().split(" ")
    last_word = words[-1]
    print(len(last_word))
    explanation = f"The last word is '{last_word}' with length {len(last_word)}."
    print(explanation)

if __name__ == "__main__":
    length_last_word("")
