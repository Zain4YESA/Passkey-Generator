import tkinter as tk
from tkinter import PhotoImage, Label, Text, Button, RAISED, END, filedialog
import random

root = tk.Tk()
root.geometry("800x600")
root.title("Passkey Generator")
root.config(background='#161717')

icon = PhotoImage(file='Airplane.png')
root.iconphoto(True, icon)

label1 = Label(root, text="Passkey Generator", font=('Futurism', 20), fg='#fcba03', bg='#161717')
label1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def Passkey():
    UPPERCASE = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    LOWERCASE = list("abcdefghijklmnopqrstuvwxyz")
    DIGITS = list("0123456789")
    SPECIAL_CHARACTERS = list("!@#$%^&*()-_=+{}[]|:;<>,.?/")

    combined_list = UPPERCASE + LOWERCASE + DIGITS + SPECIAL_CHARACTERS
    passkey = ''.join(random.choice(combined_list) for _ in range(8))

    result.delete(1.0, END)
    result.insert(END, f"Passkey: {passkey}")

def save_text():
    text = result.get("1.0", END).strip()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text)

result = Text(root, height=2, fg='#fcba03', bg='#161717', bd=7)
result.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

generate_button = Button(root, text="Generate", command=Passkey, font=('Futurism', 15), fg='#fcba03', bg='black',
                         activeforeground='#03f8fc', activebackground="black")
generate_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

save_button = Button(root, text="Save", command=save_text, font=('Futurism', 15), fg='#fcba03', bg='black',
                     activeforeground='#03f8fc', activebackground="black")
save_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

root.mainloop()



