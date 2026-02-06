from canvas import app

def clear_screen():
    for el in app.grid_slaves():
        el.destroy()

def get_current_user():
    with open("db\\current_user.txt", "r") as f:
        return f.read().strip()