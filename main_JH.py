import tkinter as tk

#JH: ALL the elements appear on the UI in the same order as the defined below. Eg. if label is defined in the end,
# it will print in the end, unless you define the attributes
jh_text="Hola Jose Maharaj"

window1=tk.Tk()
# bg_image = tk.PhotoImage(file="Biggie- pink glases and hat.png")

window1.title("Title here for Jose")
window1.minsize(width=500, height=500)


# label1=tk.Label(text=jh_text, font=("Arial",23,"bold"), image=bg_image)
label1=tk.Label(text=jh_text, font=("Arial",23,"bold"))
label1.pack()

ask=tk.Entry()
ask.pack()

def button_click():
    ask_store = ask.get() #this has to be inside the function, to grab the input. If outside, it will run but since nothing
    # is in the textbox, nothing will be captured-- due to timing
    label1["text"]=f"Hola {ask_store} Mahraj" #see how f string can be used here. Not just limit to print
    label1["font"]=("Helvetica",23,"bold")
    label1["foreground"]="Purple"


button1=tk.Button(fg="Blue", width=20,text="What's gucci?",font=("Helvetica", 22),command=button_click)
button1.pack()







window1.mainloop()