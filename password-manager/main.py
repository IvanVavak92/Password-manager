import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

BG_COLOR = "#f2e9e4"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for letter in range(nr_letters)]
    password_symbols = [choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [choice(numbers) for number in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oou", message="You left empty field.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=2)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=2)

            website_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not found", message="No data found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BG_COLOR)
logo_img = PhotoImage(file="logo.png")
# 100 100 center position
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 12), bg=BG_COLOR)
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW", padx=(5, 5))

email_label = Label(text="Email/Username:", font=("Arial", 12), bg=BG_COLOR)
email_label.grid(column=0, row=2)
email_input = Entry()
email_input.insert(0, "blbl@email.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW", padx=(5, 5))

password_label = Label(text="Password:", font=("Arial", 12), bg=BG_COLOR)
password_label.grid(column=0, row=3)
password_input = Entry(width=35)
password_input.grid(column=1, row=3, sticky="EW", padx=(5, 5))

generate_password_btn = Button(text="Generate Password", command=generate)
generate_password_btn.grid(column=2, row=3, sticky="EW", padx=(5, 5))

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=(5, 5))

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW", padx=(5, 5))

window.mainloop()
