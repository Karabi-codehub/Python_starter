#We want to create a function that: Asks the user to type a number from 1 to 9.

#Stores a secret number (we'll use the number 6).

#Compares the user's number to the secret number:If the user's number is less than 6, print: "Your guess is almost there".
                                                 #If the user's number is more than 6, print: "Your guess is higher".
                                                 #If the user's number is equal to 6, print: "Your Guess Is Correct!".

def Guessing_game(guess_number,secret_number):
    if guess_number<secret_number:   
       return "Your guess is almost there"
    elif guess_number>secret_number:   
       return "Your guess is higher"  
    else:
        return "Your Guess Is Correct!"

secret_number=6
guess_number=int(input("a number from 1 to 9:"))
result=Guessing_game(guess_number,secret_number)
print(result)