import random

sec=random.randint(1,100)
attempts=0

print("Guess the number from a range of 1 to 100")
while True:
    guess=int(input("Guess the number: "))
    attempts+=1
    if guess<sec:
        print("Go higher")
    elif guess>sec:
        print("Go lower")
    else:
        print(f"You guessed it right in {attempts} attempts")
        break