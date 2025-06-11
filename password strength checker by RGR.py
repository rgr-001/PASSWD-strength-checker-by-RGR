import tkinter as tk
import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Minimum 8 characters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add a lowercase letter.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add an uppercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add a digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add a special character.")

    if strength == 5:
        return "Strong password ✅", "green"
    elif strength >= 3:
        return "Moderate password ⚠️\n" + "\n".join(remarks), "orange"
    else:
        return "Weak password ❌\n" + "\n".join(remarks), "red"

def on_check():
    password = entry.get()
    result, color = check_password_strength(password)
    result_label.config(text=result, fg=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=on_check, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), wraplength=380, justify="left")
result_label.pack(pady=10)

root.mainloop()