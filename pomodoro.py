# 25/5 for 3 times. On the fourth time 25 work and 20 min break.
# 25/5.25/5.25/5.25/20------25/5.25/5.25/5.25/20
#1,3,5,7== 25
#2,4,6=5
#8=20
import time
import tkinter as tk

cycle_running=1
eog=False

work_time= 7
mini_brk=2
long_brk=5

window1=tk.Tk()
window1.config(width=500,height=500,bg="Lightyellow") #because we are using canvas this is no longer needed.

def start_count(time_in_sec):
    # print(total_time)
    global cycle_running
    if time_in_sec>=0:
        print ("ttttt")
        min = "{:02d}".format(time_in_sec // 60) # i did it without using time module :)
        sec = "{:02d}".format(time_in_sec % 60)
        new_time = min + ":" + sec
        # print(new_time)
        canvas1.itemconfig(timer_digits, text=new_time)
        window1.after(1000, start_count, time_in_sec - 1) #new function to learn and recursion.
        print (type(time_in_sec))
    elif time_in_sec<0:
        cycle_running += 1


#==============================================================================
#JH: MY WAY, it is working up to this point, but I do not learn anything new :) So, I will use the above.
    # while total_time>=0:
    #     # print(total_time)
    #     canvas1.itemconfig(timer_digits,text=total_time)
    #     canvas1.update_idletasks() #without this the screen does not update.
    #     # It directly shows the last value, which is 0
    #     time.sleep(1)
    #     total_time -= 1
#==============================================================================

def start():
    global eog, cycle_running, work_time, mini_brk, long_brk
    while eog==False:
        if cycle_running % 2 == 1 and cycle_running<8:
            start_count(work_time)
            print (cycle_running % 2,'asdas')
            time.sleep(2)
        elif cycle_running %2 ==0 and cycle_running<8:
            start_count(mini_brk)
            print ("2121")
        else:
            start_count(long_brk)

photo1=tk.PhotoImage(file="tomato.png")
canvas1= tk.Canvas(width=500,height=500,bg="Lightyellow",highlightthickness=0) #without highlightthickness you see a white border
canvas1.create_image(250,220,image=photo1) #the numbers are x and y
timer_digits= canvas1.create_text(250,230,text="00:00",fill="white",font=("arial",30))
canvas1.place(x=20,y=10)

label_timer=tk.Label(text="Timer", font=("Palatino", 27, "bold"), bg="Lightyellow", fg="Blue")
label_timer.place(x=220, y=70)

button_start= tk.Button(text="Start", width=5, font=("Helvetica", 22), fg="Blue", bg="white",command=start)
button_start.place(x=60, y=340)

label_check_mark=tk.Label(text="✔", font=("Palatino", 12, "bold"), bg="Lightyellow", fg="Green")
label_check_mark.place(x=200, y=360)
#for such emojis and symbols we can simply copy paste from google. Type: Label

button_reset= tk.Button(text="Reset", width=5, font=("Helvetica", 22), fg="Blue", bg="white")
button_reset.place(x=360, y=340)



window1.mainloop()