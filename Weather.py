from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

''' 
#######################
Tkinter Setup
#######################

'''
root = Tk()
root.title("Weather")
root.geometry("900x500+300+200")
root.resizable(False, False)
menubar = Menu(root)
subMenu = Menu(menubar, tearoff=0)

''' 
#######################
Get Weather
#######################

'''
def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.configure(text=current_time)
        name.configure(text="CURRENT WEATHER")
        ''' 
        #######################
        Weather API
        #######################

        ''' 
        API = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=646824f2b7b86caffec1d0b16ea77f79"
        json_data = requests.get(API).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        t.configure(text=(temp, "°"))
        c.configure(text=(condition, "|", "Temperature", "Is", temp, "°"))
        w.configure(text=(wind, "Km/H"))
        h.configure(text=(humidity, "%"))
        d.configure(text=description)
        p.config(text=(pressure, "Pa"))

    except Exception as e:
        messagebox.showerror("Weather", "Mistake In Typing City Name!")
    
''' 
#######################
Search Box
#######################

'''
search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)
textfield = tk.Entry(root, justify="center", width=17, font=("poppins",25,"bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()
search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=get_weather)
myimage_icon.place(x=400, y=34)

''' 
#######################
Logo
#######################

'''
Logo_img = PhotoImage(file="logo.png")
logo = Label(image=Logo_img)
logo.place(x=150, y=100)

''' 
#######################
Time
#######################

'''
name = Label(root, font=("arial",15,'bold'))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica",20))
clock.place(x=30, y=130)


''' 
#######################
Bottom Box
#######################

'''
Frame_img = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_img)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

''' 
#######################
Labels
#######################

'''
Label1 = Label(root, text="WIND", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
Label1.place(x=120, y=400)

Label2 = Label(root, text="HUMIDITY", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
Label2.place(x=250, y=400)

Label3 = Label(root, text="DESCRIPTION", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
Label3.place(x=430, y=400)

Label4 = Label(root, text="PRESSURE", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
Label4.place(x=650, y=400)

t = Label(font=("arial",70,'bold'), fg="#ee666d")
t.place(x=400 ,y=150)
c = Label(font=("arial",15,'bold'))
c.place(x=400, y=250)

w = Label(text=" ", font=("arial",20,'bold'), bg="#1ab5ef")
w.place(x=100, y=430)
h = Label(text=" ", font=("arial",20,'bold'), bg="#1ab5ef")
h.place(x=270, y=430)
d = Label(text=" ", font=("arial",20,'bold'), bg="#1ab5ef")
d.place(x=394, y=430)
p = Label(text=" ", font=("arial",20,'bold'), bg="#1ab5ef")
p.place(x=654, y=430)

root.mainloop()