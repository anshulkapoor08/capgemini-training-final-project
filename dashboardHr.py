import tkinter as tk
from tkinter import ttk
import subprocess

# Sample Employee Data (Replace with database)
employees = [
    ("E001", "John Doe", "john@example.com", "2024-02-10", "2024-02-20", 10, "Pending"),
    ("E002", "Jane Smith", "jane@example.com", "2024-03-05", "2024-03-15", 11, "Approved")
]

# Function to open employee details page
def open_employee_page():
    root.destroy()
    subprocess.run(["python", "employeCompany.py"])

# Create dashboard window
root = tk.Tk()
root.title("Dashboard")
root.geometry("900x500")

# Employee Table
columns = ("ID", "Name", "Email", "Start Date", "End Date", "Leave Days", "Status")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

for emp in employees:
    table.insert("", tk.END, values=emp)

table.pack(fill=tk.BOTH, expand=True)

# Button to open Employee Page
btn_add_employee = tk.Button(root, text="Add Employee Details", command=open_employee_page)
btn_add_employee.pack(side=tk.BOTTOM, anchor="se", padx=20, pady=10)

root.mainloop()
