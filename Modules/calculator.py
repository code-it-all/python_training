def addition(num1, num2):
    try:
        return num1 + num2
    except Exception as e:
        return f"Error: {e}"

def subtract(num1, num2):
    try:
        return num1 - num2
    except Exception as e:
        return f"Error: {e}"


def multipy(num1, num2):
    try:
        return num1 * num2
    except Exception as e:
        return f"Error: {e}"

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"