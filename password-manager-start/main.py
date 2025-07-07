from tkinter import *
from random import *
from traceback import print_tb
import random
import string

FONT_NAME = "Courier"
# Allowed special characters you specified
special_chars = "$#%'^()*+|=?[]_{}\\!"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def on_yes(popup):
    popup.destroy()
    save_password()
    entry_password.delete(0, END)



def on_no(popup):
    entry_password.delete(0, END)
    popup.destroy()

def generate_popup():
    popup = Toplevel()
    popup.title("AppBrewery")
    popup.geometry("350x200")
    popup.resizable(False, False)

    label_website = Label(popup, text=f"WEBSITE: {entry_website.get()}", wraplength=300, justify="center")
    label_website.place(x = 0, y= 50)

    label_email = Label(popup, text=f"EMAIL/USERNAME: {entry_email.get()}", wraplength=300, justify="center")
    label_email.place(x=0, y=75)

    label_pass = Label(popup, text=f"PASSWORD: {entry_password.get()}", wraplength=300, justify="center")
    label_pass.place(x=0, y=100)

    button_frame = Frame(popup)
    button_frame.pack(pady=10)

    btn_yes = Button(button_frame, text="Yes", width=10, command=lambda: on_yes(popup))
    btn_yes.grid(row=0, column=0, padx=10)

    btn_no = Button(button_frame, text="No", width=10, command=lambda: on_no(popup))
    btn_no.grid(row=0, column=1, padx=10)

def password_generator():
    # Random length between 8 and 32
    length = random.randint(8, 32)

    # Make sure at least one of each required category is present
    mandatory = [
        random.choice(string.ascii_letters),  # at least 1 letter (upper/lower)
        random.choice(string.digits),  # at least 1 digit
        random.choice(special_chars)  # at least 1 special char
    ]

    # Remaining characters (fill up to desired length)
    remaining_length = length - len(mandatory)
    all_chars = string.ascii_letters + string.digits + special_chars
    remaining = [random.choice(all_chars) for _ in range(remaining_length)]

    # Combine mandatory and remaining characters, then shuffle
    password_chars = mandatory + remaining
    random.shuffle(password_chars)

    return ''.join(password_chars)

def generate_password():
    password = password_generator()
    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button_function():
    generate_popup()

def save_password():
    with open("passwords_txt", "a") as file:
        file.write(f"{entry_website.get()}| {entry_email.get()}| {entry_password.get()}\n")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=100, pady=50)
window.geometry("600x500")

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
# Instead of grid, use place:
canvas.place(x=100, y=0)

#website label
title_label = Label(text="Website:",  font=(FONT_NAME, 12))
title_label.place(x=0, y=200)

#email/username label
title_label = Label(text="Email/Username:",  font=(FONT_NAME, 12))
title_label.place(x=0, y=250)

#password label
title_label = Label(text="Password:",  font=(FONT_NAME, 12))
title_label.place(x=0, y=300)

#entry widget for website
entry_website = Entry(width=50)
entry_website.place(x=160, y=200)

#entry widget for email
entry_email = Entry(width=50)
entry_email.place(x=160, y=250)

#entry widget for password
entry_password = Entry(width=50)
entry_password.place(x=160, y=300)

#generate_password button
password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password, width=65)
password_button.place(x=0, y=400)

#add details button
add_button = Button(text="add", highlightthickness=0, command=add_button_function, width = 65)
add_button.place(x=0, y=350)

window.mainloop()