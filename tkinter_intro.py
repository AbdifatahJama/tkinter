'''Uptil now all program/scripts have been made to work within the command prompt. Whereas,in modern programs use graphical user interfaces. For example: calculators, tax calculators'''

'''To create a GUI, different graphical user interfaces libaries are used. In this case uses tkinter libary. '''

import tkinter as tk # imports tkinter libary as tk
from tkinter import Button, Checkbutton, Entry, Frame, Label, Tk, ttk
from tkinter.constants import BOTTOM, CENTER, E, LEFT, N, RIGHT, TOP, W, X, Y
import random

def start():
  root = tk.Tk() # uses tk namespace to call the Tk() constructor

  '''Uses Tk() class to set GUI title and geometry'''
  root.title('First Graphical user interface')
  root.geometry('1000x500')

  '''Producing a label'''
  label = tk.Label(root,text='my label') # Label positioned within root and text in label
  '''The mainloop() method can be called to show the root window. This causes the root window to enter a event processing that listens for events. Ie: pressing buttons, writing keys into a text box'''
  label2 = tk.Label(root,text='Another label')
  label.pack() # One of three geometry managers allows widget to be controlled and positoned round the screen
  label2.pack()
  button1 = Button(root,text='Click me',padx=200,pady=200,fg='blue',bg='red')
  button1.pack(side=LEFT)
  root.mainloop()

'''Once a root window is created different buttons, text boxes, etc can be placed within the root window

HOWEVER, before this frames must be established. 
Frames are invisible containers sections(Areas) defined by the user within the GUi to place components within it

To work with frames and buttons  the ttk module must imported from tkinter
'''

'''Geometry Managar

-> Pack - Easiest geometry manager
-> Grid - you can map row and columns in a root window and specify where exactly the widgit should be in the row and columns 
-> Place - Even more control 

Note: Two or more geometry managers cannot be used for one window as each geometry has different algorithims
'''

'''Buttons
Can be created in a simalar way to labels using the required Constructor. Button()

buttons can be made iteractive using the command feature where a function can be placed within it
'''
def buttons():
  root = tk.Tk()

  root.title('Interactive button clicker')
  root.geometry('200x200')
  i = 0
  def button_click():
    button.config(text='I have been clicked')
    
  def move_button():
    '''Moves button every time it is clicked'''
    list = [RIGHT,LEFT,TOP]
    choice = random.choice(list)
    button.pack(side=choice)
  button = Button(root,text='Button',pady=50,fg='red',command=move_button)
  button.pack(side=TOP)


  root.mainloop()

'''Frames

Are invisible sections/ within the root window where widgit such a labels and buttons can be placed into. The widgits can be moved around the frame

buttons and labels inherit the frame they are in
'''
def interactive():
  
  i = 0
  def click():
    print('clicked')
      
  def clicked():
    print('Button 3 clicked')
    button3.config(text='Button clicked',padx=20,pady=20)
    
  root = tk.Tk()
  root.title('Graphical user interface')
  root.geometry('150x200')
  frame1 = Frame(root,bg='red') # Frame1 is within the root window hence inherites it
  frame2 = Frame(root) # Frame2 is within the root window hence inherites it
  frame3 = Frame(root,bg='yellow')
  '''Make button called 'click me!' '''
  button1 = Button(frame1,text='click me!',pady=10,padx=10,command=click,bg='blue')
  button1.pack()

  button2 = Button(frame2,text='click me too!',pady=10,padx=10,command=click)
  button2.pack()

  button3 = Button(frame3,text='Button 3',command=clicked)
  button3.pack(side=LEFT)

  label1 = Label(frame1,text='Label 1') 
  label2 = Label(frame2,text='Label 2')
  label3 = Label(frame3,text='Label3')

  label1.pack()
  label2.pack()
  label3.pack()

  frame1.pack()
  frame2.pack(side=BOTTOM)
  frame3.pack()



  root.mainloop()


'''Getting user inputs using the Entry constructor'''
def click():
  if len(e1.get()) >0:
    print('Your name is:',e1.get()) # gets user entry
    button.config(text='Clicked',bg='red',fg='blue')
    
  else:
    print('Invalid name')
  
def entries():
  
  root = tk.Tk()
  root.title('User inputs')
  root.geometry('200x200')

  frame1 = Frame(root)
  frame1.pack()
  label = Label(frame1,text='What is your name?',fg='red')
  button = Button(frame1,text='Click me',padx=10,pady=10,command=click)
  label.pack() # Label shown

  e1 = Entry(frame1) # Entry field that inherites frame1 and thus, is within the inivisible rectangle frame 1 along with the label entry box and button
  e1.pack() # Text box
  # button.pack() # Button

  button.pack()




  root.mainloop()


'''Using grid geometry manager to place widgits specifically based on the row and columns in the grid '''
def using_grids():
  root = Tk()
  root.title('Login page')
  root.geometry('300x300')

  email_label = Label(root,text='Email:')
  password_label = Label(root,text='Password:')

  email_entry = Entry(root)
  password_entry = Entry(root)

  '''Submit button'''
  submit_button = Button(root,text='Submit')

  '''The widgits can then be placed using the grid geometry manager'''
  email_label.grid(row=0,column=0)
  password_label.grid(row=2,column=0)

  email_entry.grid(row=0,column=1,sticky=W)
  password_entry.grid(row=2,column=1)

  submit_button.grid(row=4,column=1)

  '''Sticky allows widgits to be aligned to each other. Arguments to sticky are N,E,S,W '''
  '''Padding within an entry/button(widgit) can also be made using ipadx or ipady that pads within the widgit in the x direction or y direction'''

  '''pad argument can be used to produce padding on the outside of widgits in the x or y direction'''

  root.mainloop()

'''Widgits can be spanned over various spans or columns using the spancolumns or spanrows'''

def spans():
  root = Tk()

  root.title('App')
  root.geometry('300x200')

  email = Label(root,text='Enter your email')
  email_entry = Entry(root)
  button = Button(root,text='Submit',fg='red')
  check_button = Checkbutton(root)
  label = Label(root,text='Remember my email?')
  '''Using grid geometry manager'''
  email.grid(row=1,column=0)
  email_entry.grid(row=1,column=1,ipadx=7)
  label.grid(row=2,column=0,columnspan=1)
  check_button.grid(row=2,column=1)
  button.grid(row=3,column=1)




  root.mainloop()

'''Binding functions is a step up from using the command argument when responding to a user event. Button binding allows certain events to be binded to a certain function. Ie: left click of button submits to database and right click gets information'''

'''Event buttons are specified on this page - 'https://www.python-course.eu/tkinter_events_binds.php' '''
def button_clicked(event): # event listner function always take atleast one argument normally called event or i
  print('Button clicked')

def binding_events():
  root = Tk()
  def typing(event):
    print(entry.get() + ' ' + 'charecters')

  button = Button(root,text='Click me')
  button.bind('<Button-1>',button_clicked)
  button.pack()

  label = Label(root,text='Enter text')
  entry = Entry(root)
  entry.bind('<Key>',typing)
  label.pack()
  entry.pack()
  root.mainloop()


'''There are many event labels that can be placed on widgits

  Within this section the event labels will be used within the root 
'''
def foo(event):
  print('Event has been triggered')
  
def release(event):
  print('Button released')

def close(event):
  root.destroy() # Closes root window completely
  
root = Tk()
root.title('Event binding labels')

root.bind('<Enter>',foo) # Event is triggered everytime pointer enters root window. <Leave> is simalar and is triggered everytime the pointer leaves the root window
root.bind('<Key>',foo)
root.bind('a',foo) # Event is triggered everytime a key is typed. Could be used to produce apps that exit when Capital Q is typed 
root.bind('<Double-Button-1>',foo) # Triggers when a double click is made, 1 is double left click,2 is middle click,3 is right double click

root.bind('<ButtonRelease-1>',foo)
root.bind('Q',close) 

root.mainloop()

'''Skills shownn above are the basic and fundemantals of tkinter'''
