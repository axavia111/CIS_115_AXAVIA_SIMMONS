#The program shows whether or not the characters entered is a palindrome

word = input("Enter a word/phrase: ")

reversedString = word[::-1]

def isPalindrome():
    if (word == reversedString):
        print(f'The word/phrase {word} is a palindrome')
    else:
        print(f'The word/phrase {word} is not a palindrome')

isPalindrome()


