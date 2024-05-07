import random


score = 0
while True:
    print("Score: ", score)
    num =  random.randint(1, 20)
    print(num)
    
    like = input("do you like the number?  y/n: ")
    if like =="y":
        score = score+1
        print("you got the score.")
    else:
        print("generate another number.")

    input()
    
    