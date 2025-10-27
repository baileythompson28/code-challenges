# palindrome number         
# a word, phrase, or sequence that reads the same backward as forward.

number = input("\nEnter a number, we will determine if the number is a palindrome: -> ")
if number == number[::-1]:
    print(f"x = {number}")
    print("True, the number is a palindrome")
    print(f" - Explanation: {number} reads as {number} from left to right and from right to left.\n")
if number != number[::-1]:
    print(f"x = {number}")
    print("False, the number is not a palindrome")
    print(f" - Explanation: From left to right, it reads {number}. From right to left, it is not the same number. Therefore it is not a palindrome.\n")

