import random

def game():

    score=random.randint(1,100)
    with open ("hi_score.txt","r") as file:
        hiscore = file.read()

    with open ("hi_score.txt","w") as file:
        if(hiscore=="" or int(score)>int(hiscore)):
            file.write(str(score))
        else:
            file.write(str(hiscore))   
    print("your score:",score)
game()