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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oou", message="You left empty field.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")

email_label = Label(text="Email/Username:", font=("Arial", 12), bg=BG_COLOR)
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.insert(0, "blbl@email.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:", font=("Arial", 12), bg=BG_COLOR)
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=2, sticky="EW")

generate_password_btn = Button(text="Generate Password", command=generate)
generate_password_btn.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
