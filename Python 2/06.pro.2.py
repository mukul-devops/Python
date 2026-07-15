import random

def game():
    score = random.randint(1,60)
    print("You are playing the game")
    print(f"your's score is {score}")
    with open("hiscore.txt") as f:
        hiscore =f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
        
    return score 
        
game()

        
        

