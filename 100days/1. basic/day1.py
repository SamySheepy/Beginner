import random
secret_number = random.randint(1,10)
attempts = 3
print("I'm thinking of a number between 1 and 10.")
print("Try to guess it!")
while attempts >= 0:
    guess = int(input("Take a guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    attempts -= 1

if attempts == 0:
    print ("Sorry, you've run out of attempts. The secret number was: ", secret_number)
    