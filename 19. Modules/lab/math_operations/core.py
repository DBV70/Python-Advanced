operation_map = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y,
}

def calculate(num1, num2, operation):
    function = operation_map[operation]
    return function(num1, num2)
