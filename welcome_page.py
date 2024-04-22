import tkinter as tk
import time
import os

def proceed_to_login():
    os.system("start dashboard.py")

    
def flash_label(color_index):
    colors = ['#FF0000', '#00FF00', '#0000FF']  
    welcome_label.config(fg=colors[color_index])
    color_index = (color_index + 1) % len(colors)
    root.after(500, flash_label, color_index)  



root = tk.Tk()
root.title("Inventory Management System")
root.geometry("900x150")


root.configure(bg="#f0f0f0")
welcome_font = ("Helvetica", 24, "bold")
button_font = ("Arial", 12)


welcome_label = tk.Label(root, text="Welcome to the Inventory Management System!", font=welcome_font, bg="#f0f0f0")
welcome_label.pack(pady=30)


proceed_button = tk.Button(root, text="Proceed", command=proceed_to_login, font=button_font)
proceed_button.pack(pady=10)


flash_label(0)

root.mainloop()
