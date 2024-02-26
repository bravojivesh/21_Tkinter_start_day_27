# 25/5 for 3 times. On the fourth time 25 work and 20 min break.
# 25/5.25/5.25/5.25/20------25/5.25/5.25/5.25/20
#1,3,5,7== 25
#2,4,6=5
#8=20
import time
import tkinter as tk

cycle_running=1
eog=False

work_time= 4
mini_brk=2
long_brk=3
check_mark=""

window1=tk.Tk()
window1.config(width=500,height=500,bg="Lightyellow") #because we are using canvas this is no longer needed.

def start_count(time_in_sec):
        global cycle_running,eog
        if eog== False: #need this. Reset will set this to True, so it should not work.
                if time_in_sec >=0:
                        min = "{:02d}".format(time_in_sec // 60) # i did it without using time module :)
                        sec = "{:02d}".format(time_in_sec % 60)
                        new_time = min + ":" + sec

                        canvas1.itemconfig(timer_digits, text=new_time)
                        window1.after(200, start_count,time_in_sec-1) #new function to learn and recursion.
                        #usign this with "while" WILL CAUSE infinite loop. If the scheduling is done within the while loop,
                        # a new call to start_count is scheduled every time the loop runs,
                        # regardless of the value of time_in_sec.
                        # This causes an infinite cascade of scheduled function calls.
                        print(cycle_running)

                elif time_in_sec<0:
                        cycle_running +=1
                        print(cycle_running)
                        count()



def count():
        global cycle_running, long_brk, mini_brk, work_time,check_mark,label_check_mark,label_timer,eog
        eog=False #you have to reset this back to False when touching the button (inside this blocl).
        # If not, after reset, startign again wont work
        if cycle_running in [1,3,5,7]:
                start_count(work_time)
                label_timer.config(text="Work", fg="Red")
                label_timer.place(x=220, y=70)

        elif cycle_running in [2,4,6]:
                start_count(mini_brk)
                label_timer.place(x=200, y=70)
                label_timer.config(text="Mini Break", fg="Pink")
                check_mark += "✔"
                label_check_mark.config(text=check_mark)

        elif cycle_running ==8:
                start_count(long_brk)
                label_timer.place(x=200, y=70)
                label_timer.config(text="Long Break", fg="Grey")
                check_mark += "✔"
                label_check_mark.config(text=check_mark)


def reset1():
        global eog,cycle_running,timer_digits,check_mark

        #if you use #after.cancel() it will stop the function

        eog=True
        cycle_running=1
        canvas1.itemconfig(timer_digits,text="00:00")
        label_timer.config(text="Timer", fg="Blue")
        check_mark =""
        label_check_mark.config(text=check_mark)




photo1=tk.PhotoImage(file="tomato.png")
canvas1= tk.Canvas(width=500,height=500,bg="Lightyellow",highlightthickness=0) #without highlightthickness you see a white border
canvas1.create_image(250,220,image=photo1) #the numbers are x and y
timer_digits= canvas1.create_text(250,230,text="00:00",fill="white",font=("arial",30))
canvas1.place(x=20,y=10)

label_timer=tk.Label(text="Timer", font=("Palatino", 27, "bold"), bg="Lightyellow", fg="Blue")
label_timer.place(x=220, y=70)

button_start= tk.Button(text="Start", width=5, font=("Helvetica", 22), fg="Blue", bg="white",command=count)
button_start.place(x=60, y=340)

label_check_mark=tk.Label(text=check_mark, font=("Palatino", 12, "bold"), bg="Lightyellow", fg="Green")
label_check_mark.place(x=200, y=360)
#for such emojis and symbols we can simply copy paste from google. Type: Label

button_reset= tk.Button(text="Reset", width=5, font=("Helvetica", 22), fg="Blue", bg="white",command=reset1)
button_reset.place(x=360, y=340)



window1.mainloop()