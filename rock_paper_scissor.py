#import library
from tkinter import *
import random

#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Game - Rock, Paper, Scissor')
root.config(bg ='seashell3')

#heading
Label(root, text = 'Rock, Paper , Scissor' , font='arial 20 bold', bg = 'seashell2').pack()

#user choice
user_take= StringVar()
Label(root, text = 'Choose any one: rock, paper ,scissor' , font='arial 15 bold', bg = 'seashell2').place(x=15 , y = 80)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)

#function to play
Result = StringVar()

def play():
    user_pick = user_take.get().lower()

    #computer choice
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'rock'
    elif comp_pick ==2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissor'
    
    if user_pick == comp_pick:
        Result.set('TIE!! you both chose same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('YOU LOSE!! computer chose paper')
    elif user_pick == 'rock' and comp_pick == 'scissor':
        Result.set('YOU WIN!! computer chose scissor')
    elif user_pick == 'paper' and comp_pick == 'scissor':
        Result.set('YOU LOSE!! computer chose scissor')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('YOU WIN!! computer chose rock')
    elif user_pick == 'scissor' and comp_pick == 'rock':
        Result.set('YOU LOSE!! computer chose rock')
    elif user_pick == 'scissor' and comp_pick == 'paper':
        Result.set('YOU WIN!! computer chose paper')
    else:
        Result.set('Invalid choice: Choose any one --> rock, paper, scissor')

#fun to reset
def Reset():
    Result.set("") 
    user_take.set("")

#fun to exit
def Exit():
    root.destroy()

#button
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)

root.mainloop()
