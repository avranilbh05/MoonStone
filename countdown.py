#DataFlair Guide for Countdown Clock and Timer
#Import necessary modules
from plyer import notification 
from tkinter import messagebox
from tkinter import *
import time

#Assign class and set dimensions of the interface
window = Tk()
window.geometry("400x500")
window.title("MoonStone~ Pomodoro")
window.config(bg='black')

#Function to activate timer and show notifications once timer is up
def timer(): 

    #Since we use placeholders, we check if the user entered an integer
    try:
        timer_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())
        
    except:
        messagebox.showerror(message="Enter Valid Time")   
    if timer_time >0:
        hour = 0
        min = 0 
        sec = 0    

        while timer_time >= 0:
            min, sec = divmod(timer_time,60)
            if min > 60:
                hour, min = divmod(min,60) 
               
            hours.set(hour)
            mins.set(min)
            secs.set(sec)

            time.sleep(1)   

            window.update()

            timer_time -= 1
        #Create a desktop notification
        notification.notify(
            #Title of the notification,
            title = "TIMER ALERT",
            #Body of the notification
            message = "Hey there!\nDid you acheive it? \nIf not, try again with a new pomodoro session",
            app_icon = "/home/deepika/Downloads/internship/countdown_timer/pictures/bell.ico",
            #Notification stays for 30 seconds
            timeout  = 30,
        )

        messagebox.showinfo(message="Times Up!")         
        

def h_click(event):
        hour_entry.delete(0,'end')         
def m_click(event):
        min_entry.delete(0,'end')
def s_click(event):    
        sec_entry.delete(0,'end')
    
title_label_1 = Label(window, text="Set timer and start working,",font=("Fira Sans Compressed", 20,'bold'),bg='black',fg='white').pack(side=TOP,pady=10)
title_label_2 = Label(window, text="**Try atleast 25 mins of work",font=("Fira Sans Compressed", 13,'italic'),bg='black',fg='red').pack(side=TOP,pady=10)
title_label_3 = Label(window, text="All the best for your goal!",font=("Fira Sans Compressed", 10,'italic'),bg='black',fg='white').pack(side=BOTTOM,pady=10)

hours = IntVar()
mins = IntVar()
secs = IntVar()


hour_entry = Entry(window, width=5,textvariable=hours,font=("Fira Sans Compressed",20))
min_entry = Entry(window, width=5,textvariable=mins,font=("Fira Sans Compressed",20))
sec_entry = Entry(window, width=5,textvariable=secs,font=("Fira Sans Compressed",20))


hour_entry.insert(0,00)
min_entry.insert(0,00)
sec_entry.insert(0,00)

hour_entry.place(x=90,y=160)
min_entry.place(x=170,y=160)
sec_entry.place(x=250,y=160)


hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

button = Button(window,text='Start', bg = 'Black',fg='white',command=timer,width=10).pack(side=BOTTOM,pady=100)


window.mainloop()
