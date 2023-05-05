# Create a program that will prompt the user for a word, and return a 'word triangle'. 
# For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON

word = str(input("Please enter a word: "))
for r in range(len(word)):
    for c in range(r + 1):
        print(word[c], end=' ')
    print()