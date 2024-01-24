import tkinter as tk
from tkinter import messagebox

class ShoppingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping Application")

        # Create a dictionary to store product information
        self.products = {
            'Website domain': 10.0,
            'Website theme 2': 20.0,
            'Total workable website 3': 15.0
        }

        # Initialize variables
        self.selected_product = tk.StringVar()
        self.quantity = tk.IntVar()

        # GUI components
        tk.Label(master, text="Select Product:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.product_menu = tk.OptionMenu(master, self.selected_product, *self.products.keys())
        self.product_menu.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text="Quantity:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.quantity_entry = tk.Entry(master, textvariable=self.quantity)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(master, text="Add to Cart", command=self.add_to_cart).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(master, text="Checkout", command=self.checkout).grid(row=3, column=0, columnspan=2, pady=10)

        # Cart
        self.cart = tk.Listbox(master)
        self.cart.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_to_cart(self):
        product = self.selected_product.get()
        quantity = self.quantity.get()

        if quantity > 0:
            total_price = self.products[product] * quantity
            cart_item = f"{product} x{quantity} - ${total_price:.2f}"
            self.cart.insert(tk.END, cart_item)
        else:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")

    def checkout(self):
        total_cost = sum(float(item.split('- $')[1]) for item in self.cart.get(0, tk.END))
        messagebox.showinfo("Checkout", f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
