print("Hello git hub world")
guess = int(input('Please guess a number between 1 to 10: '))
secret_number = 3
while guess != secret_number:
    if (guess)==(secret_number):
        print("Yai !! Correct")
        print()
    elif guess > 10: 
        print("try a number smaller then 10. Try again.")
        print( )
        guess = int(input('Please guess a number between 1 to 10: '))
        print( )
    else:
        (guess) != secret_number
        print("Try again !")
        print( )
        guess = int(input('Please guess a number between 1 to 10: '))
        print()
exit


