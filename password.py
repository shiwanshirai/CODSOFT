import string
import random
import tkinter as tk

def generate_password():
    try:
        plen = int(entry.get())
        if plen < 1:
            raise ValueError("Enter the lenght of your password: ",fg="red")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")
        return

    s = []
    s1 = string.ascii_lowercase  # Lowercase letters
    s2 = string.ascii_uppercase  # Uppercase letters
    s3 = string.digits         # Digits
    s4 = string.punctuation    # Special characters
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    
    random.shuffle(s)
    password = "".join(s[0:plen])
    
    result_label.config(text=f"Generated Password: {password}", font=("Courier New",15,"bold"), fg="green")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter Password Length:", font=("Courier New", 15), fg="navy", bg="lightsteelblue").pack(pady=10)

entry = tk.Entry(root, font=("Courier New", 15), fg="black", bg="white")
entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Courier New", 15), fg="darkgreen", bg="mintcream").pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier New", 12))
result_label.pack()

root.mainloop()