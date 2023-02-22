from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pwd_letters = [random.choice(letters) for _ in range(nr_letters)]
    pwd_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pwd_num = [random.choice(numbers) for _ in range(nr_numbers)]

    pwd_list = pwd_num + pwd_letters + pwd_symbols
    random.shuffle(pwd_list)
    generated_pwd = "".join(pwd_list)

    pwd_entry.insert(0, generated_pwd)
    pyperclip.copy(generated_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = web_entry.get()
    mail = email_entry.get()
    pwd = pwd_entry.get()

    if len(web) == 0 or len(mail) == 0 or len(pwd) == 0:
        messagebox.showinfo(message="Please fill every field with details")
    else:
        is_ok = messagebox.askyesno(title=web, message=f"Do you want to save the following:\nEmail: {mail}\n"f"Password: {pwd}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web} | {mail} | {pwd}\n")
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                pwd_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=80, pady=80)
window.title("Password Manager")
# Canvas

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Label

website = Label(text="Website")
Email = Label(text="Email/Username")
password = Label(text="Password")
website.grid(row=1, column=0)
Email.grid(row=2, column=0)
password.grid(row=3, column=0)

# Entry

web_entry = Entry(width=35)
web_entry.focus()
email_entry = Entry(width=35)
pwd_entry = Entry(width=25)
web_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
pwd_entry.grid(row=3, column=1)

# Button
pwd_btn = Button(text="Generate Password", command=gen_pwd)
add_btn = Button(text="Add", width=36, command=save)
pwd_btn.grid(row=3, column=2, columnspan=2)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
