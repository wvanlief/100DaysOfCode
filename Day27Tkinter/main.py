from tkinter import *

window = Tk()

window.title("My first GUI window")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=("Times", 24, "italic"))
my_label.pack()

my_label["text"] = "New Text"


# Button


def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()

window.mainloop()
