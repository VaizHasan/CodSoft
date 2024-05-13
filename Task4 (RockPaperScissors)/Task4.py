from tkinter import *
from PIL import Image,ImageTk
import random
import time

userscore=0
pcscore=0
timeleft=60 
timerlabel=None
result=None

def enter(event):
    rock.config(bg='black',fg='white')
def enter1(event):
    paper.config(bg='black',fg='white')
def enter2(event):
    scissors.config(bg='black',fg='white')
    
def leave(event):
    rock.config(bg='white',fg='black')
def leave1(event):
    paper.config(bg='white',fg='black')
def leave2(event):
    scissors.config(bg='white',fg='black')

def starttimer():
    global timeleft, timerlabel
    timerlabel = Label(root, text=f"Time left: {timeleft} ", bg='maroon', fg='white', font='Times 16 bold')
    timerlabel.place(x=280, y=330)
    updatetimer()

def updatetimer():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timerlabel.config(text=f"Time left: {timeleft} s")
        root.after(1000, updatetimer)
    else:
        endgame()

def endgame():
    global userscore, pcscore
    winner = "Player 1" if userscore > pcscore else "Player 2" if pcscore > userscore else "It's a tie"
    result.config(text=f"Game Over! {winner} wins with a score of {max(userscore, pcscore)}")
    rock.config(state=DISABLED)
    paper.config(state=DISABLED)
    scissors.config(state=DISABLED)    

def playagain():
    global userscore, pcscore, timeleft
    userscore=0
    pcscore=0
    timeleft=60
    maingame()
    result.config(text='High Score Wins!')
    rock.config(state=NORMAL)
    paper.config(state=NORMAL)
    scissors.config(state=NORMAL)
    starttimer()

root=Tk()
root.geometry('700x500')
root.resizable(False,False)
root.title("Rock Paper Scissors Game")

bgimage = Image.open("rps.png")
bgphoto = ImageTk.PhotoImage(bgimage)
bglabel = Label(root, image=bgphoto)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

L2=Label(text=f"Your Score: {userscore}",bg='green',fg='white',font='Times 16 bold',padx=4,pady=2)
L2.grid(row=5,column=0,pady=15)
L3=Label(text=f"PC Score: {pcscore}",bg='green',fg='white',font='Times 16 bold',padx=4,pady=2)
L3.grid(row=6,column=0,pady=15)

def maingame():
    global userscore, pcscore
    L2.config(text=f"Your Score: {userscore}")
    L3.config(text=f"PC Score: {pcscore}")

def click(event):
        global userscore,pcscore  
        global L1     
        global pcchose   
        L1.grid_forget()    
        pcchose.destroy()  
        
        val=event.widget.cget('text') 

        x=random.randint(0,2)
        l1=['Rock','Paper','Scissors']
        pc_opt=l1[x] 

        pcchose=Label(text=f'PC Opted: {pc_opt}',font='Times 16 bold',bg='red',fg='white')
        pcchose.grid(row=5,column=1,pady=15)

        if val=='Rock' and pc_opt=='Paper': 
            L1=Label(text='PC Won!',font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            pcscore+=1
            
        elif val=='Rock' and pc_opt=='Scissors':
            L1=Label(text='You Won!',font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        elif val=='Paper' and pc_opt=='Scissors':
            L1=Label(text='PC Won!',font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            pcscore+=1
            
        elif val=='Paper' and pc_opt=='Rock':
            L1=Label(text='You Won!',font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        elif val=='Scissors' and pc_opt=='Rock':
            L1=Label(text='PC Won!',font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            pcscore+=1
            
        elif val=='Scissors' and pc_opt=='Paper':
            L1=Label(text='You Won!',font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        elif val==pc_opt:
            L1=Label(text="It's A Tie!",font='Times 20 bold',bg='black',fg='white')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            pcscore+=1
        maingame()

head=Label(text='Rock Paper Scissors',font='Times 20 bold',bg='maroon',fg='white')
head.grid(columnspan=2,row=0,ipadx=20,padx=200,pady=10)
playerone=Label(text=f'Player 1 : You',font='Times 16 bold',bg='maroon',fg='white')
playerone.grid(row=1,column=0)
playertwo=Label(text=f'Player 2 : Computer',font='Times 16 bold',bg='maroon',fg='white')
playertwo.grid(row=1,column=1)

rock=Button(text='Rock',font='Times 14 bold',bg='navyblue',fg='white',height=1,width=7)
rock.grid(row=2,column=0,pady=15)
rock.bind('<Enter>',enter)
rock.bind('<Leave>',leave)
rock.bind('<Button-1>',click)
paper=Button(text='Paper',font='Times 14 bold',bg='navyblue',fg='white',height=1,width=7)
paper.grid(row=3,column=0)
paper.bind('<Enter>',enter1)
paper.bind('<Leave>',leave1)
paper.bind('<Button-1>',click)
scissors=Button(text='Scissors',font='Times 14 bold',bg='navyblue',fg='white',height=1,width=7)
scissors.grid(row=4,column=0,pady=15)
scissors.bind('<Enter>',enter2)
scissors.bind('<Leave>',leave2)
scissors.bind('<Button-1>',click)

rock1=Button(text='Rock',font='Times 14 bold',bg='navyblue',fg='white',height=1,width=7)
rock1.grid(row=2,column=1,pady=15)
paper1=Button(text='Paper',font='Times 14 bold',bg='navyblue',fg='white',height=1,width=7)
paper1.grid(row=3,column=1)
scissors1=Button(text='Scissors',font='Times 14 bold',bg='navyblue',fg='white',height=1,width=7)
scissors1.grid(row=4,column=1,pady=15)

rock=Button()
paper=Button()
scissors=Button()

L1=Label()          
pcchose=Label()     

starttimer()  
result=Label(root, text='High Score Wins!', font='Times 14 bold', bg='navyblue', fg='white')
result.grid(row=10, columnspan=2, pady=40)

playagain=Button(text='Play Again', bg='maroon', fg='white', font='Times 12 bold', command=playagain)
playagain.place(x=60, y=450)

btnclose=Button(text='Exit Game',bg='maroon',fg='white',font='Times 12 bold',command=root.destroy)
btnclose.place(x=550,y=450)

root.mainloop()
