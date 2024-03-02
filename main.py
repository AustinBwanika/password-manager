from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

# # ---------------------------- UI SETUP ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for a in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
    }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Damn", message=" Fill in the blanks")
    else:
        try:
            with open("data.json", "r") as file:
                # json.dump(new_data, file, indent=4)
                # Reading old data
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            # Updates old data with the new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saves updated data
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            # email_input.delete(0, END)
            password_input.delete(0, END)



 # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)


# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password")


# Buttons
generate_button = Button(text="Generate Password", command=generate)
add_button = Button(text="Add", width=36, command=save)
search_button = Button(text="Search", command=search, width=11)

# Input
website_input = Entry(width=21)
email_input = Entry(width=38)
password_input = Entry(width=21)

# Setup
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
website_input.focus()
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_input.grid(column=1, row=1,)
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0,"dummy@gmail.com")
password_input.grid(column=1, row=3)
add_button.grid(column=1, columnspan=2, row=4)
generate_button.grid(column=2, row=3)
search_button.grid(column=2, row=1)


window.mainloop()

# window = Tk()
# window.title("Pomdoro")
# window.config(padx=100, pady=50)
# window.mainloop()