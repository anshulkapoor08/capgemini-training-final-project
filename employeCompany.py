import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to add employee details (Can be connected to a database)
def add_employee():
    messagebox.showinfo("Success", "Employee Added Successfully!")

# Function to go back to dashboard
def back_to_dashboard():
    root.destroy()
    subprocess.run(["python", "dashboardHr.py"])

# Function to open leave details page
def open_leave_page():
    root.destroy()
    subprocess.run(["python", "employeLeave.py"])

# Create Employee Page
root = tk.Tk()
root.title("Employee Details")
root.geometry("500x400")

tk.Label(root, text="Employee Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Age:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Button(root, text="Add Employee", command=add_employee).pack(pady=10)

# Buttons at the bottom
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

btn_back = tk.Button(frame, text="Back to Dashboard", command=back_to_dashboard)
btn_back.pack(side=tk.LEFT, padx=20)

btn_add_leave = tk.Button(frame, text="Add Leave Details", command=open_leave_page)
btn_add_leave.pack(side=tk.RIGHT, padx=20)

root.mainloop()
