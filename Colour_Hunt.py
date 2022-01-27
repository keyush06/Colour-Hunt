##The code is to create a colour game using Tkinter with its exceptional GUI toolkit.

from tkinter import *
import random as r
timeLeft=45
score=0
colours=["red","purple","green","yellow","orange","black","white","blue","pink","brown","light blue","grey"]

def startGame():
    global timeLeft
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

btn=Button(root,text="Press here to start the game",command=lambda:startGame(),bg="light blue")
btn.pack()

submitColour=Button(root,text="Submit Your Answer", command=lambda:submit(),bg="yellow")
submitColour.pack()

# listBox=Listbox(root)
# listBox.insert(1,"Restart")
# listBox.insert(2,"Exit")
# listBox.pack()

# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='Game Options', menu=filemenu)
# filemenu.add_command(label='Restart',command=options("Restart"))
# filemenu.add_command(label='Exit',command=options("Exit"))
# filemenu.add_separator()

e=Entry(root)
e.pack()
e.focus_set()
root.mainloop()