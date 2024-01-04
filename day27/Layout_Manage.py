from tkinter import *

window = Tk()
window.title("My Frist GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)
# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label["text"] = "New Text"
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


# Button
def clear_text():
    input.delete(0, END)


def button_clicked():
    new_text = input.get()
    clear_text()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=3, row=0)
# Entry
input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()
