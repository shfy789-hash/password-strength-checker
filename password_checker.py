import tkinter as tk

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")


label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=15)


def check_password():
    password = entry.get()
    
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    has_special = False
    has_uppercase = False
    has_digit = False
    score = 0

    for char in password:
        if char in special_characters:
            has_special = True
        if char.isupper():
            has_uppercase = True
        if char.isdigit():
            has_digit = True

    length = len(password)

    if length >= 8:
        score += 1
    if has_special:
        score += 1
    if has_uppercase:
        score += 1
    if has_digit:
        score += 1

    if length < 8:
        result_label.config(text="Result: Weak (Must be at least 8 characters)", fg="red")
    elif score == 4:
        result_label.config(text="Result: Strong", fg="green")
    elif score in (2, 3):
        result_label.config(text="Result: Medium", fg="orange")
        if not has_uppercase and not has_digit and not has_special:
            result_label.config(text="Missing Uppercase Letter, Digit, and Special Character", fg="orange")
        elif not has_uppercase and not has_digit:
            result_label.config(text="Missing Uppercase Letter and Digit", fg="orange")
        elif not has_uppercase and not has_special:
            result_label.config(text="Missing Uppercase Letter and Special Character", fg="orange")
        elif not has_digit and not has_special:
            result_label.config(text="Missing Digit and Special Character", fg="orange")
    else:
        result_label.config(text="Result: Weak", fg="red")
        if not has_uppercase and not has_digit and not has_special:
            result_label.config(text="Missing Uppercase Letter, Digit, and Special Character", fg="red")
        elif not has_uppercase and not has_digit:
            result_label.config(text="Missing Uppercase Letter and Digit", fg="red")
        elif not has_uppercase and not has_special:
            result_label.config(text="Missing Uppercase Letter and Special Character", fg="red")
        elif not has_digit and not has_special:
            result_label.config(text="Missing Digit and Special Character", fg="red")
            
check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=5)

root.mainloop()