import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

# Sample Leave Data
leave_data = [
    ("E001", "Sick Leave", "2024-02-10", "2024-02-20", 10),
    ("E002", "Annual Leave", "2024-03-05", "2024-03-15", 11)
]

# Function to delete selected leave entry
def delete_leave():
    selected_item = leave_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a leave record to delete")
        return
    leave_table.delete(selected_item)
    messagebox.showinfo("Deleted", "Leave record deleted successfully")

# Function to go back to dashboard
def back_to_dashboard():
    root.destroy()
    subprocess.run(["python", "dashboardHr.py"])

# Create Leave Page
root = tk.Tk()
root.title("Leave Details")
root.geometry("600x400")

# Leave Table
columns = ("Employee ID", "Leave Type", "Start Date", "End Date", "Days")
leave_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    leave_table.heading(col, text=col)
    leave_table.column(col, width=100)

for leave in leave_data:
    leave_table.insert("", tk.END, values=leave)

leave_table.pack(fill=tk.BOTH, expand=True)

# Buttons at the bottom
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

btn_delete = tk.Button(frame, text="Delete Leave", command=delete_leave)
btn_delete.pack(side=tk.LEFT, padx=20)

btn_dashboard = tk.Button(frame, text="Go to Dashboard", command=back_to_dashboard)
btn_dashboard.pack(side=tk.RIGHT, padx=20)

root.mainloop()
