import tkinter as tk
from tkinter import messagebox
import time

def salarycheck(func):
  def wrapper():
    salary = float(entry_salary.get())
    if salary < 25000:
      messagebox.showerror('Eligibility check', 'Salary is too low for eligibility')
    else:
      return func(salary)
  return wrapper

def loan_eligi(func):
  def wrapper(salary):
    salary_yearly = salary*12
    if salary_yearly < 300000:
      messagebox.showerror('Loan Check', 'Not eligible for loan')
    else:
      return func(salary)
  return wrapper

def timer(func):
  def wrapper(salary):
    start = time.time()
    time.sleep(2)
    result = func(salary)
    end = time.time()
    messagebox.showinfo('Execution Time', f'Time taken: {round(end-start,2)} sec')
    return result
  return wrapper

@salarycheck
@loan_eligi
@timer
def cal_emi(salary):
  try:
    p = float(entry_loan.get())
    r = float(entry_rate.get())/12/100
    t = float(entry_years.get())*12
    emi = round(p*r*(1+r)**t / ((1+r)**t - 1),2)
    result_label.config(text=f'Monthly emi: ₹{emi}')
  except:
    messagebox.showerror('Input error', 'Please fill all fields with valid numbers')

#GUI Setup
root = tk.Tk()  
root.title('Emi Calculator with Eligibility Check')
root.geometry('400x400')

tk.Label(root, text='Monthly Salary').pack()
entry_salary = tk.Entry(root)
entry_salary.pack()

tk.Label(root, text='Loan Amount').pack()
entry_loan = tk.Entry(root)
entry_loan.pack()

tk.Label(root, text='Interest rate%').pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text='Loan Tenure (Years)').pack()
entry_years = tk.Entry(root)
entry_years.pack()

tk.Button(root, text='Check & Calculate EMI', command=cal_emi).pack(pady=10)

result_label = tk.Label(root,text='',font=('Arial',12,'bold'))
result_label.pack()

root.mainloop()
