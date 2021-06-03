import random
def win(a,b):
    print("YOU WIN!")
    print("Your choice:",a,"\nComputer's choice:",b)
def lose(a,b):
    print("YOU LOST!")
    print("Your choice:",a,"\nComputer's choice:",b)
while 1:
    print("\n--------------------------\nROCK - PAPER - SCISSOR\nMake your choice:")
    data=(input("Rock / Paper / Scissor (Enter nothing to quit):"))
    if data =="":
        print("Have a good day!")
        break
    data=data.lower()
    if data not in ["rock","paper","scissor"]:
        print("Please provide valid input.")
        continue
    rnum=random.randint(0,2)
    arr=["rock","paper","scissor"]
    if data == arr[rnum]:
        print("It's a TIE")
        print("Your choice:",data,"\nComputer's choice:",arr[rnum])
        continue
    if data=="rock":
        if rnum==1:
            lose(data,arr[rnum])
        else: win(data,arr[rnum])
    elif data=="paper":
        if rnum==2:
            lose(data,arr[rnum])
        else: win(data,arr[rnum])
    else:
        if rnum==0:
            lose(data,arr[rnum])
        else: win(data,arr[rnum])
