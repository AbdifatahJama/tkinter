'''This script is an investment graphical user interface'''

from tkinter import *
from tkinter import messagebox
import locale as lc
from random import choice

lc.setlocale(lc.LC_ALL,'')

'''Script first needs to make root object using Tk class'''

root = Tk()
root.title('Investment calculator')

'''Make menu with Home,reset and exit'''

'''Menu commands'''

def reset():
  '''Function command that clears all entry widgit'''
  initial_entry.delete(0,END)
  yearly_investment_rate.delete(0,END)
  years.delete(0,END)
  
def random_initial(initial):
  '''Inserts random initial investment into initial investment entry'''
  initial_entry.insert(0,choice(initial))
  
def random_rate(rate):
  '''Insert random interest rate into yearly investment rate entry'''
  yearly_investment_rate.insert(0,choice(rate))
  
def random_year(year):
  '''Inserts random year into year entry'''
  years.insert(0,choice(year))

def random():
  initial = ['0','10','20','30','50','100','150','500','1000','5000','10000']
  rate = ['0.1','0.2','0.5','1','10','25']
  year = ['1','2','3','4','5','6','7','8','9','10','20','50','100']
  reset()
  random_initial(initial)
  random_rate(rate)
  random_year(year)
  
  
  
  
  
  
  
    
def save():
  print('Saved')
  



my_menu = Menu(root)
root.config(menu=my_menu)

home_menu = Menu(my_menu) # home menu object
reset_menu = Menu(my_menu) # reset menu object
exit_menu = Menu(my_menu)  # exit menu object
random_menu = Menu(my_menu) # random menu object

my_menu.add_cascade(label='Home',menu=home_menu)
my_menu.add_cascade(label='Reset',menu=reset_menu)
my_menu.add_cascade(label='Exit',menu=exit_menu)
my_menu.add_cascade(label='Random',menu=random_menu)
home_menu.add_command(label='Save',command=save)
reset_menu.add_command(label='Reset all fields',command=reset)
exit_menu.add_command(label='Exit now',command=root.quit)
random_menu.add_command(label='Add random number in fields',command=random)

'''This section of the script will include the main bulk of the graphical user interface'''

frame1 = Frame(root)
frame1.pack()
app_title = Label(frame1,text='Investment Graphical User interface',font=22,fg='blue')
app_title.pack()
name_title = Label(frame1,text='By Abdifatah Jama')
name_title.pack()

frame2 = Frame(root)
frame2.pack(pady=20)

initial_title = Label(frame2,text='Initial monthly investment:')
initial_title.pack()

initial_entry = Entry(frame2)
initial_entry.pack()

yearly_investment_rate_title = Label(frame2,text='Monthly Investment rate(%):')
yearly_investment_rate_title.pack()

yearly_investment_rate = Entry(frame2)
yearly_investment_rate.pack()

years_title = Label(frame2,text='Number of years investment:')
years_title.pack()

years = Entry(frame2)
years.pack()

def calc_future_value(initial,month,rate):
  future_value = 0
  for i in range(month):
    future_value += initial
    monthly_interest = future_value*rate
    future_value+=monthly_interest
  calculation_text.config(text='£'+ str(round(future_value,2)))
    
  
  
'''Calculate button'''

def calculate_button():
  '''This method is triggered after calculate button is clicked'''
  try:
    initial = int(initial_entry.get())
    rate = float(yearly_investment_rate.get())/12/100
    year = int(years.get())
    months = year*12
    return calc_future_value(initial,months,rate)
    
  except:
    messagebox.showwarning('Error. Ensure all fields are filled with the correct data type')

calculate_button = Button(frame2,text='Calculate',pady=15,padx=15,command=calculate_button)
calculate_button.pack()

'''Label that displays final calculation'''

calculation_text = Label(frame2,text='',pady=20,font=20)
calculation_text.pack()



root.mainloop()