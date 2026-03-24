from tkinter import*
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=73098f5f8572e15c6f8c8e2d448a43f1").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win =Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x570")

name_label=Label(win,text="Weather App",font=("Time New roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()

list_name=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam',
    'Bihar',
    'Chandigarh',
    'Chhattisgarh',
    'Dadra and Nagar Haveli and Daman and Diu','Goa','Gujurat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerela','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','NCT of Delhi','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal'
]
com=ttk.Combobox(win,textvariable=city_name,values=list_name,font=("Time New roman",20,"bold"))
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="Weather Climate",font=("Time New roman",17))
w_label.place(x=25,y=260,height=50,width=215)
w_label1=Label(win,text="",font=("Time New roman",17))
w_label1.place(x=250,y=260,height=50,width=215)

wb_label=Label(win,text="Weather Description",font=("Time New roman",17))
wb_label.place(x=25,y=330,height=50,width=215)
wb_label1=Label(win,text="",font=("Time New roman",17))
wb_label1.place(x=250,y=330,height=50,width=215)

temp_label=Label(win,text="temperature",font=("Time New roman",17))
temp_label.place(x=25,y=400,height=50,width=215)
temp_label1=Label(win,text="",font=("Time New roman",17))
temp_label1.place(x=250,y=400,height=50,width=215)

per_label=Label(win,text="Pressure",font=("Time New roman",17))
per_label.place(x=25,y=470,height=50,width=215)
per_label1=Label(win,text="",font=("Time New roman",17))
per_label1.place(x=250,y=470,height=50,width=215)

done_button=Button(win,text="Done",font=("Time New roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()