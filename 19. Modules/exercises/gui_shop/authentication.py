import tkinter as tk
from canvas import app
from helpers import clear_screen
from products import render_products_screen
import json
from string import punctuation

def login(username, password):
    with open("db\\user_credentials.txt", "r") as f:
        for line in f:
            user, pwd = line.strip().split(", ")
            if username == user and password == pwd:
                with open("db\\current_user.txt", "w") as cu:
                    cu.write(username)
                render_products_screen()
                return

    render_login_screen(error="Invalid credentials!")

def render_login_screen(error=None):
    clear_screen()

    tk.Label(app, text="Username: ").grid(row=0, column=0, sticky="w")
    username = tk.Entry(app)
    username.grid(row=0, column=1, width=30)

    tk.Label(app, text="Password: ").grid(row=1, column=0, sticky="w")
    password = tk.Entry(app, show="*")
    password.grid(row=1, column=1)

    tk.Button(
        app,
        text="Login",
        bg="green",
        fg="black",
        width=7,
        command=lambda: login(username.get(), password.get())
    ).grid(row=2, column=1, sticky="w")

    tk.Button(
        app,
        text="Back",
        bg="yellow",
        fg="black",
        width=7,
        command=render_main_enter_screen,
    ).grid(row=2, column=1, sticky="e")

    if error:
        tk.Label(app, text=error, fg="red").grid(row=3, column=1)

def register(**user):
    # input validation
    if user["username"] == "" or user["password"] == "" or user["first_name"] == "" or user["last_name"] == "":
        render_register_screen(error="All fields are required!")
        return
    if user["username"] == user["password"]:
        render_register_screen(error="Username and password cannot be the same!")
        return
    if len(user["password"]) < 4:
        render_register_screen(error="Password must be at least 4 characters long!")
        return
    if len(user["username"]) < 4:
        render_register_screen(error="Username must be at least 4 characters long!")
        return
    password_validation_map = {"upper": False, "lower": False, "digit": False, "special": False}
    for ch in user["password"]:
        if ch.isupper():
            password_validation_map["upper"] = True
        elif ch.islower():
            password_validation_map["lower"] = True
        elif ch.isdigit():
            password_validation_map["digit"] = True
        elif ch in punctuation:
            password_validation_map["special"] = True
    if not all(password_validation_map.values()):
        render_register_screen(error="Password must contain at least one uppercase, one lowercase, one digit and one special character!")
        return
    if len(user["first_name"]) < 2 or len(user["last_name"]) < 2:
        render_register_screen(error="First name and last name must be at least 2 characters long!")
        return

    # update user credentials
    user.update({"products": []})
    with open("db\\user_credentials.txt", "r+") as f:
        users = [line.strip().split(', ')[0] for line in f]
        if user["username"] in users:
            render_register_screen(error="User already exists!")
            return
        f.write(f"{user['username']}, {user['password']}\n")

    with open("db\\users.txt", "a") as f:
        f.write(json.dumps(user) + "\n")

    render_login_screen()

def render_register_screen(error=None):
    """Renders registration screen with input fields and error display"""
    clear_screen()

    tk.Label(app, text="User: ").grid(row=0, column=0, sticky="w")
    username = tk.Entry(app)
    username.grid(row=0, column=1)

    tk.Label(app, text="Password: ").grid(row=1, column=0, sticky="w")
    password = tk.Entry(app, show="*")
    password.grid(row=1, column=1)

    tk.Label(app, text="First Name: ").grid(row=2, column=0, sticky="w")
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=1)

    tk.Label(app, text="Last Name: ").grid(row=3, column=0, sticky="w")
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=1)

    tk.Button(
        app,
        text="Register",
        bg="green",
        fg="black",
        width=7,
        command=lambda: register(
            username=username.get(),
            password=password.get(),
            first_name=first_name.get(),
            last_name=last_name.get()
        )
    ).grid(row=4, column=1, sticky="w")

    tk.Button(
        app,
        text="Back",
        bg="yellow",
        fg="black",
        width=7,
        command=render_main_enter_screen,
    ).grid(row=4, column=1, sticky="e")

    if error:
        tk.Label(app, text=error, fg="red").grid(row=5, column=1)

def render_main_enter_screen():
    clear_screen()

    tk.Button(
        app,
        text="Login",
        fg="white",
        bg="green",
        width=7,
        command=render_login_screen,
    ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Register",
        fg="black",
        bg="yellow",
        width=7,
        command=render_register_screen,
    ).grid(row=0, column=1)
