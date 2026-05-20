# this is a Number guessing game just like Sunil Grover in kapil sharma show guessed number of Rohit SKY axar Arshdeep and Dube 


print("Welcome to kapil sharma show with sunil Grover")

Secreat_number = 7 #thala for a reason 
print("You have total 5 attempts to guess the number correctly")
attempt = 5
while attempt >  0:
    Guess = int(input("Choose the number between 1 to 10 "))
    if Secreat_number == Guess:
        print("Congratulations! You guessed the number correctly.")
    elif Secreat_number > Guess:
        print("Increase the number")
    elif Secreat_number < Guess:
        print("Dectrase the number")       
    else:
        print("Welcome to looser world")     
    attempt = attempt - 1
    if attempt == 0:
        print("Game Over! You've used all your attempts.")
        break    