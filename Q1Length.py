# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

finished = False
while not finished:
    print("Note: To end the program, type 'quit'.")
    word = str(input("Please enter a word: "))
    if word == "quit":
        finished = True
    else: 
        print("The length of your word is: " + str(len(word)))