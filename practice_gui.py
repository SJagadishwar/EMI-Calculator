import tkinter as tk
from tkinter import messagebox
import time

def checksalary(func):
    def wrapper():
        salary = float(entry_salary.get())
        if salary < 25000:
            messagebox.showerror('salarycheck', 'Salary too low for getting loan')
        else:
            return func(salary)
    return wrapper

def loanamt(func):
    def wrapper(salary):
        annual_salary = salary*12
        if annual_salary < 300000:
            messagebox.showerror('Eligibility check', 'Not Eligible for Loan')
        else:
            return func(salary)
    return wrapper

def timer(func):
    def wrapper(salary):
        start = time.time()
        time.sleep(2)
        result = func(salary)
        end = time.time()
        messagebox.showinfo('Execution Time', f'Time taken: {round(end -start,2)} sec')
        return result
    return wrapper

@checksalary
@loanamt
@timer
def emical(salary):
    try:
        p = float(entry_amount.get())
        r = float(entry_rate.get())/12/100
        t = float(entry_years.get())*12
        emi = round(p * r *(1 + r)**t / ((1 + r)**t - 1),2)
        result_label.config(text=f'Monthly EMI: ₹{emi}')
    except:
        messagebox.showerror('Input Error', 'Please fill all fields with valid numbers')

#GUI SETUP
root = tk.Tk()
root.title('EMI calculator eligible check')
root.geometry('400x400')

tk.Label(root, text='Monthly Salary').pack()
entry_salary = tk.Entry(root)
entry_salary.pack()

tk.Label(root, text='Loan Amount').pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text='Interest rate(%)').pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text='Number of Years').pack()
entry_years = tk.Entry(root)
entry_years.pack()

tk.Button(root, text='Calculate EMI', command=emical).pack(pady=10)

result_label = tk.Label(root, text='',font=('Arial', 12, 'bold'))
result_label.pack()

root.mainloop()