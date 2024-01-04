from tkinter import *

window = Tk()
window.title("My Frist GUI Program")
window.minsize(width=500, height=300)
# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
# Đặt label vào màn hình và tự động canh giữa
my_label.pack()
# my_label.pack(side="left")
# my_label.pack(expand=True)
my_label["text"] = "New Text"


# Button
def clear_text():
    input.delete(0, END)


def button_clicked():
    new_text = input.get()
    clear_text()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=50)
input.pack()

# import turtle
# tim = turtle.Turtle()
# tim.write("Some Text", font=("Times New Roman", 80, "bold"))
window.mainloop()
