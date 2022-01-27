##The code is to create a colour game using Tkinter with its exceptional GUI toolkit.

from cgitb import text
from tkinter import *
import random as r
timeLeft=45
score=0
colours=["red","purple","green","yellow","orange","black","white","blue","pink","brown","light blue","gray","violet"]

def startGame():
    global timeLeft
    timeLeft=45
    if timeLeft==45:
        countdown()
        nextColour()


def submit():
    nextColour()

def countdown():
    global timeLeft
    if timeLeft>0:
        timeLeft-=1
        time_label.config(text="Time left: "+str(timeLeft))
        time_label.after(1000,countdown)



def nextColour():
    global timeLeft
    global score
    if timeLeft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1
        if e.get().lower()=='exit':
            root.destroy()
        e.delete(0,END)
        r.shuffle(colours)
        score_label.config(text="Score: "+str(score))
        colourChange.config(fg=str(colours[1]),text=str(colours[0]))

def options(ans):
    if ans=="Restart":
        startGame()
    elif ans=="Exit":
        root.destroy()


#DRIVER CODE
root=Tk()

root.title("Colour Hunt")

root.geometry("800x300")

time_label= Label(root,text="Time Left=0",fg="red",font=("helvetica",20))
time_label.pack()

score_label=Label(root,text="Score: "+str(score),font=("helvetica",16),fg="black")
score_label.pack()

instructions=Label(root,text="TYPE THE COLOUR OF THE TEXT AND NOT THE NAME OF THE COLOUR ITSELF", font=("algerian",15))
instructions.pack()

colourChange=Label(root,font=("Helvetica",60))
colourChange.pack()

btn=Button(root,text="Press here to start/restart the game & Input exit to end!",command=lambda:startGame(),bg="green")
btn.pack()

submitColour=Button(root,text="Submit Your Answer", command=lambda:submit(),bg="yellow")
submitColour.pack()

e=Entry(root)
e.pack()
e.focus_set()
root.mainloop()