import tkinter as tk
from tkinter import messagebox,ttk
import sqlite3

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()
        
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)
        
        self.label_description = tk.Label(root, text="Description:")
        self.label_description.grid(row=1, column=0)
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row=1, column=1)
        
        self.label_quantity = tk.Label(root, text="Quantity:")
        self.label_quantity.grid(row=2, column=0)
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=2, column=1)
        
        self.label_price = tk.Label(root, text="Price:")
        self.label_price.grid(row=3, column=0)
        self.entry_price = tk.Entry(root)
        self.entry_price.grid(row=3, column=1)
        
        self.button_add = tk.Button(root, text="Add Product", command=self.add_product)
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.label_product_id = tk.Label(root, text="Product ID:")
        self.label_product_id.grid(row=5, column=0)
        self.entry_product_id = tk.Entry(root)
        self.entry_product_id.grid(row=5, column=1)
        
        self.button_delete = tk.Button(root, text="Delete Product", command=self.delete_product)
        self.button_delete.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.label_search_name = tk.Label(root, text="Search Name:")
        self.label_search_name.grid(row=7, column=0)
        self.entry_search_name = tk.Entry(root)
        self.entry_search_name.grid(row=7, column=1)
        
        self.label_search_price = tk.Label(root, text="Search Price:")
        self.label_search_price.grid(row=8, column=0)
        self.entry_search_price = tk.Entry(root)
        self.entry_search_price.grid(row=8, column=1)
        
        self.button_search = tk.Button(root, text="Search", command=self.search_product)
        self.button_search.grid(row=9, column=0, columnspan=2, pady=10)


        self.button_display = tk.Button(root, text="Display Items", command=self.display_table)
        self.button_display.grid(row=11, column=0, columnspan=2, pady=10)

    def add_product(self):
        """Add a new product to the inventory."""
        name = self.entry_name.get()
        description = self.entry_description.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()
        
        if name and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)
                # Insert the product into the database
                self.cursor.execute("INSERT INTO items (name, description, quantity, price) VALUES (?, ?, ?, ?)", (name, description, quantity, price))
                self.conn.commit()
                messagebox.showinfo("Success", "Product added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Quantity and Price must be numeric.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    def delete_product(self):
        """Delete a product from the inventory."""
        product_id = self.entry_product_id.get()
        if product_id:
            try:
                product_id = int(product_id)
                # Delete the product from the database
                self.cursor.execute("DELETE FROM items WHERE id=?", (product_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Product deleted successfully!")
            except ValueError:
                messagebox.showerror("Error", "Product ID must be numeric.")
        else:
            messagebox.showerror("Error", "Please enter a product ID.")
    
    def search_product(self):
        """Search for a product by name and price."""
        name = self.entry_search_name.get()
        price = self.entry_search_price.get()
        
        if name and price:
            try:
                price = float(price)
                # Search for the product in the database
                self.cursor.execute("SELECT * FROM items WHERE name=? AND price=? AND quantity>0", (name, price,))
                result = self.cursor.fetchone()
                if result:
                    messagebox.showinfo("Product Found", "Product found and available.")
                else:
                    messagebox.showinfo("Product Not Found", "Product not found or not available.")
            except ValueError:
                messagebox.showerror("Error", "Price must be numeric.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    def display_table(self):
        """Display all items in the inventory."""
        # Retrieve data from the database
        self.cursor.execute("SELECT * FROM items")
        items = self.cursor.fetchall()
        
        # Create a new window to display the table
        table_window = tk.Toplevel(self.root)
        table_window.title("Items Table")
        
        # Create a Treeview widget
        tree = ttk.Treeview(table_window, columns=("ID", "Name", "Description", "Quantity", "Price"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Description", text="Description")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        
        # Insert data into the Treeview
        for item in items:
            tree.insert("", "end", values=item)
        
        tree.pack(expand=True, fill="both")
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
