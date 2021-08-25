'''Weight tracker graphical user interface that allows a user to input to enter their weight once a day. Only one exception button that allows user to append latest weight if their is mistake'''

import tkinter as tk
from tkinter import Label, PanedWindow, Widget, ttk
from tkinter.constants import FALSE
from datetime import datetime,date
from weightDatabase import Database
import matplotlib.pyplot as plt

class CreateFrame1(ttk.Frame):
  '''Creates frame '''
  def __init__(self, master):
    ttk.Frame.__init__(self,master,padding='10 10 10 10')
    self.pack() # Packs frame into root window
    self.create_title()
    
  def create_title(self):
    '''Creates title of the graphical user interface'''
    ttk.Label(self,text='Weight tracker').pack()

class CreateFrame2(ttk.Frame):
  '''creates frame that inherites Frame widget'''
  def __init__(self,master): # takes master/root argument 
    ttk.Frame.__init__(self,master,padding='10 10 10 10')
    self.pack(expand=True)
    self.create_label()
    self.create_entry()
    self.create_button()
    self.add_padding()
    self.date_now = datetime.now()
    self.date_now_fully_formatted = datetime.strftime(self.date_now,'%d/%m/%Y %H:%M')
    self.hour_now = datetime.strftime(self.date_now,'%H')
    self.hour_int = int(self.hour_now) # When intantiated, current hour integer is calculated
    print('Hour now:',self.hour_int)
    
  def create_label(self):
    '''Creates label to that refers to entry box'''
    ttk.Label(self,text='Add your current weight').grid(column=0,row=0)
    l1 = ttk.Label(self,text='Click to show graph of your weight')
    l1.grid(column=1,row=3)
    l1.bind('<Button-1>',self.show_plot)

  def create_entry(self):
    self.weight_string = tk.StringVar()
    '''Creates entry box that allows user to enter their weight'''   
    ttk.Entry(self,textvariable=self.weight_string).grid(column=1,row=0)
    
  def create_button(self):
    '''creates button needed to submit and change latest weight submitted'''
    ttk.Button(self,text='Submit weight',command=self.add_weight_to_database).grid(column=1,row=1)
    ttk.Button(self,text='Change latest weight').grid(column=1,row=2)
    
  def add_weight_to_database(self):
    '''if conditions are satisfied users weight is added into the table within database with the current date'''
    if self.weight_string.get().isdigit():
      '''if block triggered if entered weight is a digit'''
      d = Database() # instantiates database module that connects to weight database
      d.add_user(self.date_now_fully_formatted,int(self.weight_string.get())) # adds data into table within database
      self.weight_string.set('')
    else:
      print('Please enter your weight in number representation')
      
  def show_plot(self,event):
    '''Shows date series plot when show graph label is right clicked. This will show the data within database in plotted form using matplotlib'''
    d = Database()
    data = d.get_all_rows() # returns a list object with tuple item within it
    dates_str = []
    weights = []
    for dates,weight in data:
      '''for loop to loop the content of each tuple item within the list and append them in the nessecary list'''
      dates_str.append(dates)
      weights.append(weight)
      
    '''dates within dates list need to be converted from string to datetime object'''
    
    datetime_list =  [datetime.strptime(date,'%d/%m/%Y %H:%M') for date in dates_str] # using list comprehension 
    plt.plot_date(datetime_list,weights,linestyle = 'solid',color = 'black')
    plt.title('Weight Tracker')
    plt.xlabel('Date')
    plt.ylabel('Weight(Kg)')
    plt.tight_layout()
    '''Set range of xaxis'''
    plt.gcf().autofmt_xdate() # Rotates date a suitable way to avoid conjestion on the x axis
    plt.show()
    
  def show_graph_window(self,event):
    '''Shows graph window'''
    top_window = tk.Toplevel(self.master)
    top_window.geometry('500x500')
    new_window = NewWindow(top_window)
    top_window.mainloop()
    
  def add_padding(self):
    '''Adds padding in all child widgets in frame'''
    for child in self.winfo_children():
      if isinstance(child,ttk.Button):
        pass
      
      else:
        child.grid_configure(padx=5,pady=5)
        
class NewWindow(ttk.Frame):
  '''Making frame that is within the new top level window'''
  def __init__(self, master):
    '''Initialises master which in this case is the new window '''
    ttk.Frame.__init__(self,master,padding='10 10 10 10') # Frame class takes the master argument new_window
    self.pack(expand=True) # Packs frame within new window
    self.make_canvas()
    
  def make_canvas(self):
    '''Making canvas within frame inside top_window root'''
    my_canvas = tk.Canvas(self,bg='white',width=400,height=400)
    my_canvas.pack(pady=10,padx=10)
    my_canvas.create_arc(1,1,500,500)
    
    
      
    
    
        
root = tk.Tk() # Creates root window
root.title('Weight tracker')
root.iconbitmap('dumbells (1).ico') # iconbitmap can only take images with suffix ".ico" which is a file type that supports icons
c1 = CreateFrame1(root)
c2 = CreateFrame2(root)
root.mainloop()





