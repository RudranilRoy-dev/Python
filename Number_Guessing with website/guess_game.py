import random
import time

print("Welcome to the Number Guess Game!")
time.sleep(2)
print("\nHow to Play:")
time.sleep(3)
print("\nComputer will generate a number in (0-10000)")
time.sleep(4)
print("\nThen, You need to guess the number")
time.sleep(4)
print("\nIf you will guess bigger\nThen it will shows\nYou choosed bigger number")
time.sleep(4)
print("\nIf you will guess smaller\nThen it will shows \nYou choosed smaller number.")
time.sleep(4)
print("\nMin Number of Attempt will be the High Score\n")
time.sleep(4)
print("Okk let's Play....")

highscore=10000
while(1):
    attempts=0
    number= int(random.randint(0,10000))
    while (1):
        user = int(input("\nEnter number:"))
        attempts+=1
        if user==number:
            print("Checking....")
            time.sleep(1)
            print(f"\nYour guess is correct 😉!\nThe number is:{number}\nYou took {attempts} attempts.")
            break
        elif user>number:
            print("Checking....")
            time.sleep(1)
            print("\nYou choosed a bigger number:)")
        else:
            print("Checking....")
            time.sleep(1)
            print("\nYou choosed a smaller number:)")

    if attempts<highscore or attempts==highscore:
        highscore=attempts

    print("\nHigh Score is: ",highscore)

    replay=int(input("\nFor Play Again Enter - 0\nFor Exit Enter - 1\nEnter Your choice:"))
    if replay==1:
        time.sleep(1)
        print("Exited...")
        break
    elif replay != 0 and replay != 1:
        print ("\nSOMETHING WENT WRONG")
        time.sleep(1)
        print("Exited...")
        break