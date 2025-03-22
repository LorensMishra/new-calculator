import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Function to set theme
def set_theme(theme):
    if theme == "dark":
        root.configure(bg="#2E2E2E")
        style.configure("TButton", background="#555555", foreground="#FFFFFF", font=("Times New Roman", 10))
        style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF", font=("Times New Roman", 10))
        style.configure("TEntry", fieldbackground="#555555", foreground="#FFFFFF", font=("Times New Roman", 10))
    elif theme == "light":
        root.configure(bg="#F0F0F0")
        style.configure("TButton", background="#DDDDDD", foreground="#000000", font=("Times New Roman", 10))
        style.configure("TLabel", background="#F0F0F0", foreground="#000000", font=("Times New Roman", 10))
        style.configure("TEntry", fieldbackground="#FFFFFF", foreground="#000000", font=("Times New Roman", 10))
    elif theme == "blue":
        root.configure(bg="#E6F3FF")
        style.configure("TButton", background="#99C2FF", foreground="#000000", font=("Times New Roman", 10))
        style.configure("TLabel", background="#E6F3FF", foreground="#000000", font=("Times New Roman", 10))
        style.configure("TEntry", fieldbackground="#FFFFFF", foreground="#000000", font=("Times New Roman", 10))

    # Update all windows
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.configure(bg=style.lookup("TLabel", "background"))
            for widget in window.winfo_children():
                if isinstance(widget, (ttk.Button, ttk.Label, ttk.Entry)):
                    widget.configure(style="TButton" if isinstance(widget, ttk.Button) else "TLabel" if isinstance(widget, ttk.Label) else "TEntry")


# Simple Calculator
def simple_calculator():
    def calculate():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            operator = entry_operator.get()

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Division by zero!")
                    return
            else:
                messagebox.showerror("Error", "Invalid operator!")
                return

            label_result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    simple_window = tk.Toplevel(root)
    simple_window.title("Simple Calculator")
    simple_window.geometry("300x200")

    ttk.Label(simple_window, text="First Number:").pack()
    entry_num1 = ttk.Entry(simple_window)
    entry_num1.pack()

    ttk.Label(simple_window, text="Operator (+, -, *, /):").pack()
    entry_operator = ttk.Entry(simple_window)
    entry_operator.pack()

    ttk.Label(simple_window, text="Second Number:").pack()
    entry_num2 = ttk.Entry(simple_window)
    entry_num2.pack()

    ttk.Button(simple_window, text="Calculate", command=calculate).pack()

    label_result = ttk.Label(simple_window, text="Result: ")
    label_result.pack()


# Modern Calculator
def modern_calculator():
    def calculate():
        try:
            expression = entry_expression.get()
            result = eval(expression)
            label_result.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")

    modern_window = tk.Toplevel(root)
    modern_window.title("Modern Calculator")
    modern_window.geometry("300x150")

    ttk.Label(modern_window, text="Enter Expression:").pack()
    entry_expression = ttk.Entry(modern_window)
    entry_expression.pack()

    ttk.Button(modern_window, text="Calculate", command=calculate).pack()

    label_result = ttk.Label(modern_window, text="Result: ")
    label_result.pack()


# Exchange Rate Calculator
def exchange_rate_calculator():
    def convert():
        try:
            amount = float(entry_amount.get())
            from_currency = entry_from.get().upper()
            to_currency = entry_to.get().upper()

            # Example exchange rates
            exchange_rates = {
                'USD': 1.0,
                'EUR': 0.85,
                'GBP': 0.75,
                'INR': 84.0,
            }

            if from_currency in exchange_rates and to_currency in exchange_rates:
                rate = exchange_rates[to_currency] / exchange_rates[from_currency]
                converted_amount = amount * rate
                label_result.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                messagebox.showerror("Error", "Unsupported currency.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    exchange_window = tk.Toplevel(root)
    exchange_window.title("Exchange Rate Calculator")
    exchange_window.geometry("300x200")

    ttk.Label(exchange_window, text="Amount:").pack()
    entry_amount = ttk.Entry(exchange_window)
    entry_amount.pack()

    ttk.Label(exchange_window, text="From Currency (e.g., USD):").pack()
    entry_from = ttk.Entry(exchange_window)
    entry_from.pack()

    ttk.Label(exchange_window, text="To Currency (e.g., EUR):").pack()
    entry_to = ttk.Entry(exchange_window)
    entry_to.pack()

    ttk.Button(exchange_window, text="Convert", command=convert).pack()

    label_result = ttk.Label(exchange_window, text="Result: ")
    label_result.pack()


# Age Calculator
def age_calculator():
    def calculate():
        try:
            birth_date = entry_birthdate.get()
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            label_result.config(text=f"Your age is: {age} years")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")

    age_window = tk.Toplevel(root)
    age_window.title("Age Calculator")
    age_window.geometry("300x150")

    ttk.Label(age_window, text="Enter Birth Date (YYYY-MM-DD):").pack()
    entry_birthdate = ttk.Entry(age_window)
    entry_birthdate.pack()

    ttk.Button(age_window, text="Calculate Age", command=calculate).pack()

    label_result = ttk.Label(age_window, text="Result: ")
    label_result.pack()


# Loan Calculator
def loan_calculator():
    def calculate():
        try:
            principal = float(entry_principal.get())
            rate = float(entry_rate.get()) / 100
            years = int(entry_years.get())

            monthly_rate = rate / 12
            months = years * 12
            monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
            label_result.config(text=f"Monthly Payment: {monthly_payment:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    loan_window = tk.Toplevel(root)
    loan_window.title("Loan Calculator")
    loan_window.geometry("300x200")

    ttk.Label(loan_window, text="Loan Amount:").pack()
    entry_principal = ttk.Entry(loan_window)
    entry_principal.pack()

    ttk.Label(loan_window, text="Annual Interest Rate (%):").pack()
    entry_rate = ttk.Entry(loan_window)
    entry_rate.pack()

    ttk.Label(loan_window, text="Loan Term (Years):").pack()
    entry_years = ttk.Entry(loan_window)
    entry_years.pack()

    ttk.Button(loan_window, text="Calculate", command=calculate).pack()

    label_result = ttk.Label(loan_window, text="Result: ")
    label_result.pack()


# Temperature Calculator
def temperature_calculator():
    def convert():
        try:
            temp = float(entry_temp.get())
            unit = entry_unit.get().upper()

            if unit == 'C':
                fahrenheit = (temp * 9/5) + 32
                label_result.config(text=f"{temp}°C = {fahrenheit}°F")
            elif unit == 'F':
                celsius = (temp - 32) * 5/9
                label_result.config(text=f"{temp}°F = {celsius}°C")
            else:
                messagebox.showerror("Error", "Invalid unit. Use C or F.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    temp_window = tk.Toplevel(root)
    temp_window.title("Temperature Calculator")
    temp_window.geometry("300x150")

    ttk.Label(temp_window, text="Temperature:").pack()
    entry_temp = ttk.Entry(temp_window)
    entry_temp.pack()

    ttk.Label(temp_window, text="Unit (C or F):").pack()
    entry_unit = ttk.Entry(temp_window)
    entry_unit.pack()

    ttk.Button(temp_window, text="Convert", command=convert).pack()

    label_result = ttk.Label(temp_window, text="Result: ")
    label_result.pack()


# Weight Calculator
def weight_calculator():
    def convert():
        try:
            weight = float(entry_weight.get())
            unit = entry_unit.get().lower()

            if unit == 'kg':
                pounds = weight * 2.20462
                label_result.config(text=f"{weight} kg = {pounds:.2f} lb")
            elif unit == 'lb':
                kilograms = weight / 2.20462
                label_result.config(text=f"{weight} lb = {kilograms:.2f} kg")
            else:
                messagebox.showerror("Error", "Invalid unit. Use kg or lb.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    weight_window = tk.Toplevel(root)
    weight_window.title("Weight Calculator")
    weight_window.geometry("300x150")

    ttk.Label(weight_window, text="Weight:").pack()
    entry_weight = ttk.Entry(weight_window)
    entry_weight.pack()

    ttk.Label(weight_window, text="Unit (kg or lb):").pack()
    entry_unit = ttk.Entry(weight_window)
    entry_unit.pack()

    ttk.Button(weight_window, text="Convert", command=convert).pack()

    label_result = ttk.Label(weight_window, text="Result: ")
    label_result.pack()


# Main Application
root = tk.Tk()
root.title("Multi-Calculator Project")
root.geometry("500x550")

# Style Configuration
style = ttk.Style()
style.theme_use("clam")

# Theme Buttons
ttk.Button(root, text="Dark Mode", command=lambda: set_theme("dark")).pack(pady=5)
ttk.Button(root, text="Light Mode", command=lambda: set_theme("light")).pack(pady=5)
ttk.Button(root, text="Blue Mode", command=lambda: set_theme("blue")).pack(pady=5)

# Menu Buttons
ttk.Button(root, text="Simple Calculator", command=simple_calculator).pack(pady=5)
ttk.Button(root, text="Modern Calculator", command=modern_calculator).pack(pady=5)
ttk.Button(root, text="Exchange Rate Calculator", command=exchange_rate_calculator).pack(pady=5)
ttk.Button(root, text="Age Calculator", command=age_calculator).pack(pady=5)
ttk.Button(root, text="Loan Calculator", command=loan_calculator).pack(pady=5)
ttk.Button(root, text="Temperature Calculator", command=temperature_calculator).pack(pady=5)
ttk.Button(root, text="Weight Calculator", command=weight_calculator).pack(pady=5)
ttk.Button(root, text="Exit", command=root.quit).pack(pady=5)

# Set default theme
set_theme("light")

root.mainloop()