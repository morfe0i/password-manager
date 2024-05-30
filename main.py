# ---------------------------- LIBRARIES ------------------------------- #
import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8,10))]
    symbols_list = [choice(symbols) for _ in range(randint(2,4))]
    numbers_list = [choice(numbers) for _ in range(randint(2,4))]
    
    password = letter_list + symbols_list + numbers_list
    
    
    shuffle(password)
    final_pass = ''.join(password)
    pyperclip.copy(final_pass)
    password_input.delete(0,END)
    password_input.insert(0,final_pass)
# ---------------------------- SEARCH BUTTON ------------------------------- #
def search():
    try:
        with open("G:\Python Learning\Tkinter\Password Manager\data.json", "r") as file:
            json_data = json.load(file)
            email = json_data[website_input.get()]["email"]
            password = json_data[website_input.get()]["password"]
        messagebox.askokcancel(title="Found", message= f"Email : {email} \nPassword : {password}")
    except FileNotFoundError:
        messagebox.askokcancel(title="Error", message= f"File Not Found")
    except KeyError:
        messagebox.askokcancel(title="Error", message= f"Website Not Found")
        

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_name = website_input.get()
    username = email_input.get()
    password = password_input.get()
    new_data = {
        web_name: {
        "email" : username,
        "password" : password,
    }}
    
    if len(web_name) == 0 or len(username) == 0 or len(password) == 0:
        is_empty = messagebox.askokcancel(title="Empty Fields", message= f"Please Fill All The Fields")
    
    else:
        try:
            with  open('G:\Python Learning\Tkinter\Password Manager\data.json', 'r') as file:
                data = json.load(file) #--> read data
        except FileNotFoundError:
            with  open('G:\Python Learning\Tkinter\Password Manager\data.json', 'w') as file:
                json.dump(new_data, file, indent=4) #--> write the data
        else:
            data.update(new_data) # --> update the data with the new entries
            with  open('G:\Python Learning\Tkinter\Password Manager\data.json', 'w') as file:
                json.dump(data, file, indent=4) #--> write the data
        finally:
            website_input.delete(0,END)
            email_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- COLORS & FONT ------------------------------- #
BABY_BLUE = "#75C2F6"
NAVY = "#1D5D9B"
YELLOW = "#F4D160"
LIGHTYELLOW = "#FBEEAC"
FONT = ("Arial", 10, "bold")
NAMEFONT = ("Corrier", 30, "bold")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50, bg=LIGHTYELLOW)

logo = PhotoImage(file = "G:\Python Learning\Tkinter\Password Manager\logo.png")
canvas = Canvas(width=200, height=200, bg=LIGHTYELLOW , highlightthickness=0)
canvas.create_image(100,100, image=logo)
canvas.grid(column=0,row=0)
#grid(column=,row=)

app_name = Label()
app_name.config(text="Password \nManager", bg = LIGHTYELLOW, font=NAMEFONT, fg=YELLOW)
app_name.grid(column=1,row=0, columnspan=2)

website_label = Label()
website_label.config(text="Website", bg=LIGHTYELLOW, font=FONT, fg= NAVY)
website_label.grid(column=0,row=1)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1,row=1, columnspan=2,sticky="EW")

website_btn = Button()
website_btn.config(text="Search", command=search)
website_btn.grid(column=2,row=1, sticky="EW")


email_label  = Label()
email_label.config(text="Email/Username", bg=LIGHTYELLOW, font=FONT, fg= NAVY)
email_label.grid(column=0,row=2)

email_input = Entry(width=35)
email_input.insert(0,"example@example.com")

email_input.grid(column=1,row=2, columnspan=2,sticky="EW")

password_label  = Label()
password_label.config(text="Password", bg=LIGHTYELLOW, font=FONT, fg= NAVY)
password_label.grid(column=0,row=3)

password_input = Entry(width=21, justify='left')
password_input.grid(column=1,row=3, sticky="EW")

password_btn = Button()
password_btn.config(text="Generate Password", command=gen_password)
password_btn.grid(column=2,row=3, sticky="EW")

add_btn = Button()
add_btn.config(text="Add", width=45, command=save)
add_btn.grid(column=1,row=4, columnspan=2)






window.mainloop()