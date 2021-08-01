'''This script will be a weather app graphic user interface that allows user to enter their city to find the weather conditions at that particular moment'''

from tkinter import * 
import requests
import json
import csv
from tkinter import messagebox



'''Producing graphical user interface by making root object using Tk class'''

root = Tk()
root.title('Weather graphical user interface')

frame1 = Frame(root)
frame1.pack(ipady=20)
label = Label(frame1,text='Weather Graphical User Interface',fg='blue',font=20)
label.pack()
name = Label(frame1,text='By Abdifatah Jama')
name.pack()

frame2 = Frame(root)
frame2.pack()

'''Making entry to city for particular city'''
city_label = Label(frame2,text='City name:')
city_label.grid(row=3,column=1)
city_entry = Entry(frame2,cursor='arrow')
city_entry.grid(row=3,column=3)

city_name_label = Label(frame2,text='',font=16)
city_temp = Label(frame2,text='')
city_pressure = Label(frame2,text='')
city_humidity = Label(frame2,text='')
city_name_label.grid(row=5,column=3,pady=30)
city_temp.grid(row=6,column=3)
city_pressure.grid(row=7,column=3)
city_humidity.grid(row=8,column=3)


def get_info(event):
  '''Gets info'''
  city_name = city_entry.get()
  '''Parameter dict changes the city name API parameter and includes the required API key needed for each user to identify themeselves'''
  parameter = {
    "q":city_name
  }
  try:
    '''Following block is tried, if an exception is raided the exception block is triggered'''
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?appid=21cdb87edb7fabe11cd37067db09359a&units=metric',params=parameter)
    response = response.json() # Gets JSON response for particular city simalar to json.loads
    cityName = response['name']
    cityTemp = response['main']['temp']
    cityPressure = response['main']['pressure'] 
    cityHumidity = response['main']['humidity']
    '''Data from API congifiguated in each label'''
    city_name_label.config(text=cityName)
    city_temp.config(text="Temprature:"+str(cityTemp))
    city_pressure.config(text="Pressure:"+str(cityPressure))
    city_humidity.config(text="Humidity:"+ str(cityHumidity))
  except:
    '''Exception block triggered if their is an exception in the try block. Excpetion triggers warning message box '''
    messagebox.showwarning('Invalid city name inputted')

frame3 = Frame(root,bg='blue')
frame3.pack(pady=150)
confirm_button = Button(frame3,text='Confirm')
confirm_button.grid(row=7,column=6)
confirm_button.bind('<Button-1>',get_info)

root.mainloop()
    

