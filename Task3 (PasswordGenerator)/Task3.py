from customtkinter import *
import pyperclip
import customtkinter
from tkinter import messagebox
import random

main=CTk()
main.geometry("400x420+350+150")
main.resizable(False,False)
main.configure(fg_color='black')
main.title("Password Generator")

def sliderevent(value):
    lenLabel.configure(text=int(value))

name=CTkLabel(main,text='Password Generator',font=('Times',30,'bold'),fg_color='#1F51FF',text_color='white')
name.pack(side=TOP,fill=BOTH)

frameMain=CTkFrame(main,height=400,border_color='white',border_width=2,fg_color='black')
frameMain.pack(side=BOTTOM,fill=BOTH,padx=10,pady=10)

lengthLabel=CTkLabel(frameMain,text='Password Length',text_color='white',font=('Times',20,'bold'))
lengthLabel.place(x=10,y=80)
slider=CTkSlider(frameMain,height=20,width=340,progress_color='#1F51FF',button_color='white',button_hover_color='grey',
                 number_of_steps=10,from_=5,to=15,command=sliderevent)
slider.place(x=2,y=110)

lenLabel=CTkLabel(frameMain,text='10',text_color='white',font=('Times',20,'bold'))
lenLabel.place(x=350,y=105)

radioVar1=StringVar()
radioVar2=StringVar()
radioVar3=StringVar()
count1=0
count2=0
count3=0
def radioEvent1():
    global count1,radio1
    count1=count1+1
    if count1>1:
        radio1.destroy()
        radio1=CTkRadioButton(frameMain,text='Include Numbers',hover_color='grey',fg_color='#1F51FF',border_color='#1F51FF',border_width_checked=8,width=30,height=40,font=('Times',20,'bold','italic'),value='1',variable=radioVar1,command=radioEvent1)
        radio1.place(x=80,y=140)
        radio1.deselect()
        count1=0
def radioEvent2():
    global count2,radio2
    count2=count2+1
    if count2>1:
        radio2.destroy()
        radio2=CTkRadioButton(frameMain,text='Include Alphabets',hover_color='grey',fg_color='#1F51FF',border_color='#1F51FF',border_width_checked=8,width=30,height=40,font=('Times',20,'bold','italic'),value='1',variable=radioVar2,command=radioEvent2)
        radio2.place(x=80,y=180)
        radio2.deselect()
        count2=0
def radioEvent3():
    global count3,radio3
    count3=count3+1
    if count3>1:
        radio3.destroy()
        radio3=CTkRadioButton(frameMain,text='Include Symbols',hover_color='grey',fg_color='#1F51FF',border_color='#1F51FF',border_width_checked=8,width=30,height=40,font=('Times',20,'bold','italic'),value='1',variable=radioVar3,command=radioEvent3)
        radio3.place(x=80,y=230)
        radio3.deselect()
        count3=0

radio1=CTkRadioButton(frameMain,text='Include Numbers',hover_color='grey',width=30,height=40,border_color='#1F51FF',border_width_checked=8,
                      fg_color='#1F51FF',font=('Times',20,'bold','italic'),value='1',variable=radioVar1,command=radioEvent1)
radio1.place(x=80,y=140)
radio2=CTkRadioButton(frameMain,text='Include Alphabets',hover_color='grey',width=30,height=40,border_color='#1F51FF',border_width_checked=8,
                      fg_color='#1F51FF',font=('Times',20,'bold','italic'),value='1',variable=radioVar2,command=radioEvent2)
radio2.place(x=80,y=180)
radio3=CTkRadioButton(frameMain,text='Include Symbols',hover_color='grey',border_color='#1F51FF',border_width_checked=8,
                      fg_color='#1F51FF',font=('Times',20,'bold','italic'),value='1',variable=radioVar3,command=radioEvent3)
radio3.place(x=80,y=230)

def generatePassword():
    pwd=[]
    characters=[chr(i) for i in range(65,91)]
    l2=[chr(j) for j in range(97,123)]
    characters.extend(l2)
    symbols=['_','@','?','&','#','$','!','%']
    for i in range(9):
        for i in (random.sample(symbols,1)):
            symbols.append(i)
    num=[str(i) for i in range(0,10)]
    for i in range(5):
        for i in (random.sample(num,1)):
            num.append(i)

    length=int(lenLabel.cget('text'))

    if (radioVar1.get()=='1'):
        if radioVar2.get()=='1' and radioVar3.get()=='1':
            num.extend(characters)
            num.extend(symbols)
            pwd=random.sample(num,length)
        elif radioVar2.get()=='1':
            num.extend(characters)
            pwd=random.sample(num,length)
        elif radioVar3.get()=='1':
            num.extend(symbols)
            pwd=random.sample(num,length)
        else:
            pwd=random.sample(num,length)

    elif radioVar2.get()=='1':
        if radioVar3.get()=='1':
            characters.extend(symbols)
            pwd=random.sample(characters,length)
        else:
            pwd=random.sample(characters,length)

    elif radioVar3.get()=='1':
        pwd=random.sample(symbols,length)

    else:
        messagebox.showerror('Error','Please Select atleast one option')
        return
    finalPwd=''.join(pwd)
    paslabel.configure(text=finalPwd)
    
generateButton=CTkButton(frameMain,text='Generate Password',border_color='white',border_width=1,height=40,font=('Times',25,'bold'),fg_color='#1F51FF',hover_color='grey',command=generatePassword)
generateButton.place(x=80,y=280)

paslabel=CTkLabel(frameMain,text='',font=('Times',20,'bold'),height=30,width=300,fg_color='white',text_color='black',corner_radius=5)
paslabel.place(x=20,y=30)

def copyPwd():
    pwd=paslabel.cget('text')
    pyperclip.copy(pwd)
    if pwd=='':
        pass
    else:
        messagebox.showinfo('Alert','Password Copied!')

copyButton=CTkButton(frameMain,text='Copy',height=20,width=10,border_width=1,fg_color='#1F51FF',hover_color='grey',command=copyPwd)
copyButton.place(x=325,y=35)

main.mainloop()

