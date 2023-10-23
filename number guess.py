import random
n=random.randrange(1,10)
guess=int(input("Enter any number:"))
while n!=guess:
    if guess < n:
        print("Small Number pick")
        guess=int(input("Enter number again:"))
    elif guess > n:
        print("Large number pick")
        guess=int(input("Enter number again:"))
    else:
        break
print("You Guessed the right number!!")            
        