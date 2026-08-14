# Day 29 - Password Manager
# Working with Python tkinter for practice
# Note: Do NOT use as a legitimate password manager!!! This is just a coding practice.

import json
import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    password_list += [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            email_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- Search ---------------------------------#


def search_info():
    website = web_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        messagebox.showinfo(
            title="Found Info",
            message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}",
        )
    except FileNotFoundError:
        messagebox.showinfo(
            title="No File",
            message="No passwords found. Please save login information.",
        )
    except KeyError:
        messagebox.showinfo(title="No Record", message="Record for Website not found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=pass_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
web_input = Entry(width=24)
web_input.grid(row=1, column=1)
web_input.focus()
web_btn = Button(text="Search", highlightthickness=0, command=search_info, width=15)
web_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_input = Entry(width=24)
pass_input.grid(row=3, column=1)
pass_btn = Button(
    text="Generate Password", highlightthickness=0, command=generate_password
)
pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", highlightthickness=0, width=40, command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
