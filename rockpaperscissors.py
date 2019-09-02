def game():
    print("ROCK, PAPAER, SCISSORS")
    user=input("Choose from rock, paper, scissors")
    import random
    mylist=["rock","paper","scissors"]
    comp=random.choice(mylist)
    print("player 2:",comp)
    if(user==comp):
        print("it's a tie")
    elif(user=="rock"):
        if(comp=="paper"):
            print("you win")
        else:
            print("you lose")
    elif(user=="paper"):
        if(comp=="rock"):
            print("you win")
        else:
            print("you lose")
    elif(user=="scissors"):
        if(comp=="paper"):
            print("you win")
        else:
            print("you lose")
    else:
        pass
    inp=input("Do you want to play again?(y/n)")
    if(inp=="y"):
        game()
    else:
        pass
game()
