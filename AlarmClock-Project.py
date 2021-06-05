#                                                  *Welcome to Alarm Clock*

#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

#set alarm timer from user input 
def alarm(set_alarm_timer):
    while True:
        #the loop repeats every 1 sec to check if the set time is equal to the current time
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            freq = 500
            dur = 300
            # loop iterates 8 times i.e, 8 beeps will be produced of varying frequencies and duration.
            for i in range (0,8):
                winsound.Beep(freq,dur)
                freq += 100
                dur += 100
            break

#snooze for 1 minute after alarm timer
def snooze():
        print("The alarm is Snoozed")
        time.sleep(60)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Snooze Date is:",date)
        print(now)
        print("Time to Wake up")
        freq = 500
        dur = 300
        # loop iterates 8 times i.e, 8 beeps will be produced of varying frequencies and duration.
        for i in range (0,8):
            winsound.Beep(freq,dur)
            freq += 100
            dur += 100

# Asking user to set alarm time in 24 hour format and verifying whether it is correct or not:
def actual_time():
    if int(hour.get()) not in range(0, 24)  or int(min.get()) not in range(0, 60) or int(sec.get()) not in range(0 , 60):
         print("Error. Wrong Time Entered! Please enter again!")
    else:
        set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
        alarm(set_alarm_timer)

# Initialise tkinter:
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="black",font="Arial").place(x=100,y=120)
addTime = Label(clock,text = "Hour   Min      Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "WHEN TO WAKE UP",fg="blue",relief = "solid",font=("Arial",7,"bold")).place(x=10, y=30)

# The Variables required to set the alarm (initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=190,y=30)

# To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

# To set snooze of 1 minute:
final = Button(clock,text = "Snooze",fg="red",width = 10,command = snooze).place(x =200,y=70)

clock.mainloop()
# Execution of the window.

