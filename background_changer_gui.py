'''This script is a simple graphical user interface that changes the root window background color with a press of a button'''

from tkinter import *

root = Tk()

def change_to_red():
  root.config(bg='red')
  
def change_to_orange():
  root.config(bg='orange')
  
def change_to_green():
  root.config(bg='green')
  
def change_to_purple():
  root.config(bg='purple')
  
def change_to_yellow():
  root.config(bg='yellow')

def change_to_black():
  root.config(bg='black')
  
button1 = Button(root,text='red',bg='red',command=change_to_red)
button2 = Button(root,text='orange',bg='orange',command=change_to_orange)
button3 = Button(root,text='green',bg='green',command=change_to_green)
button4 = Button(root,text='purple',bg='purple',command=change_to_purple)
button5 = Button(root,text='yellow',bg='yellow',command=change_to_yellow)

button1.pack(pady=20)
button2.pack(pady=20)
button3.pack(pady=20)
button4.pack(pady=20)
button5.pack(pady=20)



root.mainloop()