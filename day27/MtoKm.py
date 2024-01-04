from tkinter import *

window = Tk()
window.minsize(width=200, height=200)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# Label
Label_Mike = Label(text="Miles", font=("Arial", 14))
Label_Mike.grid(column=2, row=0)

Label_text = Label(text="is equal to")
Label_text.grid(column=0, row=1)

Label_Kilometer = Label(text="Km")
Label_Kilometer.grid(column=2, row=1)
# Entry
entry = Entry(width=15)
entry.grid(column=1, row=0)

entry_result = Entry(width=15, justify="center")
entry_result.grid(column=1, row=1)


def set_entry_value(kilometer):
    entry_result.delete(0, END)
    entry_result.insert(0, kilometer)


def Calculate():
    miles = float(entry.get())
    kilometer = miles * 1.609
    set_entry_value(kilometer)


# Button
button = Button(text="Calculate", command=Calculate)
button.grid(column=1, row=2)

window.mainloop()
