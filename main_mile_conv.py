import tkinter as tk

window1=tk.Tk()
window1.minsize(width=220, height=90)

ask=tk.Entry(width=7)
ask.grid(column=4, row=4)

label_miles=tk.Label(text="Miles")
label_miles.grid(column=5,row=4)

label_iseq=tk.Label(text="is equal to", padx=10)
label_iseq.grid(column=3,row=5)


total=0

label_res=tk.Label(text=total)
label_res.grid(column=4,row=5)

label_km=tk.Label(text="km")
label_km.grid(column=5,row=5)


def cal():
    miles=int(ask.get())
    result = miles * 1.6
    label_res["text"]= result


button_calc=tk.Button(fg="Blue", width=10,text="What's gucci?",font=("Helvetica", 10), command=cal)
button_calc.grid(column=4, row=6)

window1.mainloop()