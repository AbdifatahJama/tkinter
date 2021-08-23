from user_info import Database 
import tkinter as tk
from tkinter import Tk, ttk
import re

# def make_account(event):
#   print('h')

class App(ttk.Frame):
  def __init__(self,master):
    ttk.Frame.__init__(self,master,padding='10 10 10 10')
    self.master = master
    self.userName_text = tk.StringVar()
    self.password_text = tk.StringVar()
    self.pack(expand=True)
    self.create_labels()
    self.create_entry()
    self.create_button()
    self.make_account_text()
    self.add_padding()
    
    
    
  def create_labels(self):
    '''Creates labels'''
    ttk.Label(self,text='Username').grid(column=0,row=0)
    ttk.Label(self,text='Password').grid(column=0,row=1)
    
  def create_entry(self):
    '''Create entry boxes'''
    ttk.Entry(self,textvariable=self.userName_text,width=25).grid(column=1,row=0)
    ttk.Entry(self,textvariable=self.password_text,width=25,show='*').grid(column=1,row=1)
    
  def create_button(self):
    '''Creates Login button'''
    ttk.Button(self,text='Login',command=self.button_command).grid(column=1,row=3)
    
  def button_command(self):
    '''Method to check if username and password is in the database'''
    if self.userName_text.get() == '' and self.password_text.get() == '':
      print('Both Entry boxes are empty')
      
    else:
      d = Database()
      rows = d.get_all_rows()
      print(rows)
      '''Using list comprehension to append username and passwords into lists'''
      usernames = [username for row,email,username,password in rows]
      passwords = [password for row,email,username,password in rows]
      '''Then want to check if username is username. Then check if password is in the same index position as the username. Ie: if username in usernamames list then the password must be in the same index in the password if not wrong password'''
      if self.userName_text.get() in usernames:
        '''Then want to check if the connected password to the username is in the password list at the same index as the username'''
        index = usernames.index(self.userName_text.get())
        password = passwords[index]
        if password == self.password_text.get():
          print('Succesfully Logged in')
          self.destroy() # Destroys frame in root window. Self key word refers to the frame within the root window
          ttk.Label(self.master,text=self.userName_text.get() + ' ' + 'Welcome!').grid(column=4,row=4)
          
        else:
          print('Wrong password')
                    
      else:
        '''else block triggered if entered username not in usernames list then you do not have an account is triggerd'''
        print('User does not have an account')
        
      
      
  def add_padding(self):
    '''Adds padding to all children widgets within frame'''
    for child in self.winfo_children():
      child.grid_configure(padx=10,pady=10)
      
  def make_account_text(self):
    label1 = ttk.Label(self,text='Click here if you do not have an account',foreground='#4f555e')
    label1.bind('<Button-1>',self.make_account)
    label1.grid(column=1,row=4)
    
  def make_account(self,event): 
    '''Makes another window level above the root'''
    top_window = tk.Toplevel(self.master) # Creates Top Level window "root" which inherites root window
    new_window = NewWindow(top_window) # New window frame inherites Top level window as its within the top level root window
    top_window.mainloop()      # when opened window enteres into mainloop allowing it to stay opem
    

class NewWindow(ttk.Frame):
  '''Making frame that is within the new top level window'''
  def __init__(self, master):
    '''Initialises master which in this case is the new window '''
    ttk.Frame.__init__(self,master,padding='10 10 10 10') # Frame class takes the master argument new_window
    self.pack(expand=True) # Packs frame within new window
    self.make_labels()
    self.create_entry()
    self.create_button()
    self.add_padding_in_frame()

    
  def make_labels(self):
    '''Makes labels for user'''
    ttk.Label(self,text='Email Address').grid(column=0,row=0) # self key word refers to the frame within the new_window
    ttk.Label(self,text='User Name').grid(column=0,row=1)
    ttk.Label(self,text='Password').grid(column=0,row=2)
    ttk.Label(self,text='Confirm Password').grid(column=0,row=3)
    
  def create_entry(self):
    '''Creates entry boxes within frame and sets StringVariables'''
    self.email = tk.StringVar()
    self.userName = tk.StringVar()
    self.password = tk.StringVar()
    self.confirm_password = tk.StringVar()
    
    ttk.Entry(self,textvariable=self.email).grid(column=1,row=0)
    ttk.Entry(self,textvariable=self.userName).grid(column=1,row=1)
    ttk.Entry(self,textvariable=self.password,show='*').grid(column=1,row=2)
    ttk.Entry(self,textvariable=self.confirm_password,show='*').grid(column=1,row=3)
    
  def create_button(self):
    '''Creates sign up button'''
    ttk.Button(self,text='Create!',command=self.information_parse).grid(column=1,row=4)
    
  def information_parse(self):
    '''Parses user information into sqlite database'''
    self.email_list = []
    self.username_list = []
    d = Database()
    rows = d.get_all_rows() # Gets all rows in table within database
    self.email_list = [email for row,email,username,password in rows] # Uses list comprehension
    self.username_list = [username for row,email,username,password in rows]
    if self.email.get() == '' and self.userName.get() == '' and self.password.get() == '' and self.confirm_password.get() == '':
      print('All fields are empty')
      
    elif self.email.get() in self.email_list:
      print('Email is already registered with an account')
      
    elif self.userName.get() in self.username_list:
      print('Username already taken')
      
    elif self.check_password() == self.confirm_password.get() and self.email.get() not in self.email_list and self.userName.get() not in self.username_list:
      d.add_user(self.email.get(),self.userName.get(),self.password.get())
      print('User addded')
      
  def check_password(self):
    '''methods checks if password is atleast 6 charecters contains atleast one uppercase and one special charecter
    
    Uses Regex to ensure password is valid and meet requirements
    '''
    if (len(self.password.get())<6 or len(self.password.get())>12):
      #4
      print("Not valid ! Total characters should be between 6 and 12")
    elif not re.search("[A-Z]",self.password.get()):
      #5
      print("Not valid ! It should contain one letter between [A-Z]")
    elif not re.search("[a-z]",self.password.get()):
      #6
      print("Not valid ! It should contain one letter between [a-z]")
    elif not re.search("[1-9]",self.password.get()):
      #7
      print("Not valid ! It should contain one letter between [1-9]")
    elif not re.search("[~!@#$%^&*.]",self.password.get()):
      #8
      print("Not valid ! It should contain at least one letter in [~!@#$%^&*.]")
    elif re.search("[\s]",self.password.get()):
      #9
      print("Not valid ! It should not contain any space")
    else:
      #10
      is_valid = True
      return self.password.get() # returns valid password
    
  def add_padding_in_frame(self):
    '''Adding padding to children widgets within frame'''
    for child in self.winfo_children():
      child.grid_configure(padx=5,pady=5)
    
    
root = tk.Tk()
a = App(root)
root.mainloop()
