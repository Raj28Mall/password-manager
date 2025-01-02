import tkinter
from tkinter import ttk, END, messagebox
import pandas as pd
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    p1=[random.choice(letters) for _ in range(nr_letters)]
    p2=[random.choice(symbols) for _ in range(nr_symbols)]
    p3=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=p1+p2+p3
    random.shuffle(password_list)

    gen_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, gen_password)
    pyperclip.copy(password_entry)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().strip()
    email = email_combobox.get().strip()
    password = password_entry.get().strip()
    
    if not website or not email or not password:
        messagebox.showinfo(title='Oops', message='Dont leave any fields empty!')
        return
    
    is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n Do you want to save this data?")

    if is_ok:
        final_data = {
        'Website': [website],
        'Email/Username': [email],
        'Password': [password]
        }
        final = pd.DataFrame(final_data)
        
        try:
            with open('data.csv', 'r') as f:
                header = False 
        except FileNotFoundError:
            header = True  
        
        final.to_csv('data.csv', mode='a', index=False, header=header)
    
    website_entry.delete(0, END)
    email_combobox.set('rajmall.0206@gmail.com')
    password_entry.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
lock_img=tkinter.PhotoImage(file='./logo.png')
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=tkinter.Canvas(width=200, height=200)
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)

website_label=tkinter.Label(text='Website: ', pady=5)
website_label.grid(column=0, row=1)
website_entry=tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_options=['rajmall.0206@gmail.com', 'raj282bss@gmail.com']
email_label=tkinter.Label(text='Email/Username: ', pady=5)
email_label.grid(column=0, row=2)
email_combobox =ttk.Combobox(window, values=email_options, width=34)
email_combobox.set(email_options[0]) 
email_combobox.grid(column=1, row=2, columnspan=2)

password_label=tkinter.Label(text='Password: ',pady=5)
password_label.grid(column=0, row=3)
password_entry=tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)
generate_button=tkinter.Button(text='Generate Password', pady=1, padx=1, command=generate)
generate_button.grid(column=2, row=3)

add_button=tkinter.Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
