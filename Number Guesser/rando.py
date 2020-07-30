import random


def guesser():
    rando = random.randint(1, 10)
    print(rando)

    attempts = 10
    while attempts > 0:
        print(f"You Have {attempts} attempts")
        try:
            print("Guess the number! ")
            userguess = int(input())
            if userguess == rando:
                print("You guessed it correct. Congrats and good-bye!!")
                break
            elif userguess > rando:
                attempts = attempts - 1
                print(
                    f"A little to high. You have {attempts} more attempts, Try again")
            elif rando > userguess:
                attempts = attempts - 1
                print(
                    f"A little to low, You have {attempts} more attempts, Try again")
        except ValueError:
            print("Please pick an actual number. ")


guesser()
