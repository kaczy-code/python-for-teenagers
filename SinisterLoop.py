# Create an empty variable. We will store data in it later.

numberGuess = ''

# create a while loop that continues until the user enters the number 42

while numberGuess != '42':
    print("Sinister Loop stands before you!")
    print("I'll only let you capture me if you can guess the number in my brain!")
    print("Enter a number between 0 and 4 gajillion:")
    numberGuess = input() # Stores the number the user types into numberGuess

print("Sinister Loop screams in agony!")
print("How did you guess the number in his head was " + numberGuess + "?")
