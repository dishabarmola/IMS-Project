import tkinter as tk
import os

   
def open_add_product_page():
    os.system("start gui.py")

def open_delete_product_page():
    os.system("start gui.py")

def open_search_product_page():
    os.system("start gui.py")


root = tk.Tk()
root.title("Inventory Management Homepage")
root.geometry("500x100")



add_product_button = tk.Button(root, text="Add Product", command=open_add_product_page)
add_product_button.pack(side=tk.LEFT, padx=5, pady=5)

delete_product_button = tk.Button(root, text="Delete Product", command=open_delete_product_page)
delete_product_button.pack(side=tk.LEFT, padx=5, pady=5)

search_product_button = tk.Button(root, text="Search Product", command=open_search_product_page)
search_product_button.pack(side=tk.LEFT, padx=5, pady=5)


root.mainloop()