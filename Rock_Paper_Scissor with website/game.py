import random

i=1
while (i):
    computer= random.choice([1,2,3])
    user=int(input("For Rock - 1\nFor Paper - 2\nFor Scissor - 3\nFor Exit - 4\nEnter your choice (number) : "))

    if(user==4):
        break

    dic={1:"Rock",2:"Paper",3:"Scissor"}
    print(f"\nYour Choice: {dic[user]}\nComputer Choice: {dic[computer]}")

    if(computer==user):
        print("Its a Draw.\n")
    else:
        if(computer==1 and user==2):
            print("You Win!\n")

        elif(computer==1 and user==3):
            print("Computer Win!\n")

        elif(computer==2 and user==1):
            print("Computer Win!\n")

        elif(computer==2 and user==3):
            print("You Win!\n")

        elif(computer==3 and user==1):
            print("You Win!\n")

        elif(computer==3 and user==2):
            print("Computer Win!\n")

        else:
            print("Something went wrong!\n")