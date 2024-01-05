from tkinter import *

FONT = ("Courier", 15)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
img = PhotoImage(file="./day29/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(font=FONT, text="Website:")
website.grid(column=0, row=1)
email = Label(font=FONT, text="Email/Username:")
email.grid(column=0, row=2)
password = Label(font=FONT, text="Password:")
password.grid(column=0, row=3)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password")
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=36)
button_add.grid(column=1, row=4)


window.mainloop()
