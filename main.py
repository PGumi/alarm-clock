import datetime
import time
from tkinter import *
import pyttsx3 as tts
window = Tk()
window.title('alarm clock')
window.geometry("400x300")
window.config(bg = '#5B5D74')
speechEngine = tts.init()
speechEngine.setProperty("rate", 130)
voices = speechEngine.getProperty('voices')
speechEngine.setProperty('voice',voices[1].id)
speechEngine.say('here is the snooze program')
speechEngine.runAndWait()
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(window,width = 10, font =('broadway', 30, 'bold'), text = '', fg = 'white' ,bg ='#5B5D74')
curr_time.place(x = 60 , y = 10)
clock()


def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if (alarmtime != "::"):
        alarmclock(alarmtime)


def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alarmtime:
            speechEngine.say('Wake up! Wake up! Wake up! Wake up! Wake up! Wake up')
            speechEngine.runAndWait()
            break


hrs = StringVar()
mins = StringVar()
secs = StringVar()

heading = Label(window, font=('algerian', 25, 'bold'),bg ='#5B5D74',text="set a nap")
heading.place(x=130, y=90)
hours= Entry(window, textvariable=hrs, width=3, font=('arial', 25, 'bold'))
hours.place(x=110, y= 150)
minutes = Entry(window, textvariable=mins,width=3, font=('arial', 25, 'bold'))
minutes.place(x=180,y=150)
seconds = Entry(window, textvariable=secs,width=3, font=('arial', 25, 'bold'))
seconds.place(x=250,y=150)

key = Button(window, text="RUN", command=setalarm, bg="DodgerBlue2",fg="white", font=('arial', 20, 'bold'))
key.place(x=150,y=230)


mainloop()