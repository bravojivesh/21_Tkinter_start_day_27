from tkinter import *

x=0 #will be used to make the string change dynamically
y = 22 #will be used to make the string SIZE dynamic
string="jasdas"

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=700, height=700)

#Labels
label = Label(text="This is old text")
label.config(text="This is new2 text") #shows how this line overwrites the one above
label.pack()

#Buttons
def action():  #this has to come first, or else the code will error out
    # print("Do something")
    global x,y
    x+=1
    y*=1.05
    label.config(text=f"I am changing {x} no of times",font=("Helvetica", int(y))) #

#calls action() when pressed
button = Button(text="Click Me", command=action,width=20,font=("Helvetica", 22),fg="Blue",bg="white")
button.pack()


#Entries
entry = Entry(width=20, font=("Helvetica", 22))
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=50)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=108, variable=radio_state, command=radio_used)
#the value is what the .get() command receives when this radio button is selected. It has to be a floating point.

radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=8)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

