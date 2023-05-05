# Create a program that will accept a word and output the word one letter at a time in reverse.

word = str(input("Please enter a word: "))
reverse = word[::-1]
for i in reverse:
    print(i)
