import os
import json
import tkinter as tk
from PIL import Image, ImageTk
from canvas import app
from helpers import clear_screen, get_current_user

base_folder = os.path.dirname(__file__)

def update_current_user(username, product_id):
    with open("db\\users.txt", "r+") as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(user) + "\n" for user in users])
                return

def purchase_product(product_id):
    with open("db\\products.txt", "r+") as f:
        products = [json.loads(p.strip()) for p in f]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(p) + "\n" for p in products])
                return

def buy_product(product_id):
    clear_screen()
    username = get_current_user()
    purchase_product(product_id)
    update_current_user(username, product_id)
    render_products_screen()

def add_product(name, img_path, count):
    with open("db\\products.txt", "r+") as f:
        if name == "" or img_path == "" or not count.isdigit() or int(count) < 0:
            render_add_product_screen(error="All fields are required! Count must be a positive integer!")
            return
        f.write(json.dumps({
            "id": len(f.readlines()) + 1,
            "name": name,
            "img_path": img_path,
            "count": int(count)}) + "\n")
    render_products_screen()

def render_add_product_screen(error=None):
    clear_screen()

    tk.Label(app, text="Product Name: ").grid(row=0, column=0, sticky="w")
    name = tk.Entry(app)
    name.grid(row=0, column=1, sticky="w")

    tk.Label(app, text="Product Image: ").grid(row=1, column=0, sticky="w")
    image = tk.Entry(app)
    image.grid(row=1, column=1, sticky="w")

    tk.Label(app, text="Product Count: ").grid(row=2, column=0, sticky="w")
    count = tk.Entry(app)
    count.grid(row=2, column=1, sticky="w")

    tk.Button(
        app,
        text="ADD",
        bg="red",
        fg="white",
        width=7,
        command=lambda: add_product(name.get(), image.get(), count.get())
    ).grid(row=3, column=1, sticky="w")

    tk.Button(
        app,
        text="Back",
        bg="yellow",
        fg="black",
        width=7,
        command=render_products_screen,
    ).grid(row=3, column=1, sticky="e")

def render_products_screen():
    clear_screen()
    from authentication import render_main_enter_screen
    username = get_current_user()
    with open("db\\users.txt", "r") as f:
        users = [json.loads(u.strip()) for u in f]
        user = next((u for u in users if u["username"] == username and u["is_admin"]), None)
        if user:
            tk.Button(
                app,
                text="ADD",
                bg="red",
                fg="white",
                width=7,
                command=render_add_product_screen
            ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Back",
        bg="yellow",
        fg="black",
        width=7,
        command=render_main_enter_screen,
    ).grid(row=0, column=1)

    with open("db\\products.txt", "r") as f:
        products = [json.loads(p.strip()) for p in f]
        products = [p for p in products if p["count"] > 0]
        products_per_row = 6
        rows_per_product = len(products[0])
        # Renders product grid with images and purchase buttons
        for i, product in enumerate(products):
            row = i // products_per_row * rows_per_product + 1 # because of the add product button
            col = i % products_per_row

            tk.Label(app, text=product["name"], font=("Arial", 10, "bold")).grid(row=row, column=col)

            img = Image.open(os.path.join(base_folder, "db\\images\\" + product["img_path"]))
            img = img.resize((100, 100))
            photo_img = ImageTk.PhotoImage(img)
            img_label = tk.Label(app, image=photo_img)
            img_label.image = photo_img
            img_label.grid(row=row + 1, column=col)

            tk.Label(app, text=product['count'], font=("Arial", 10)).grid(row=row + 2, column=col)

            tk.Button(
                app,
                text=f"BUY",
                bg="green",
                fg="white",
                width=7,
                command=lambda p=product["id"]: buy_product(p)
            ).grid(row=row + 3, column=col)
