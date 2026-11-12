def calculator_decorator(func):
    def wrapper(expression):
        try:
            expression = expression.replace("x", "*")
            expression = expression.replace(":", "/")
            result = func(expression)
            print(f"{expression} = {result}")
            return result
        except ZeroDivisionError:
            print("Error: division by zero")
        except SyntaxError:
            print("Error: invalid expression")
        except NameError:
            print("Error: unknown variable in expression")
        except Exception as e:
            print(f"Error: {e}")
    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


calculate("2 + 2")
calculate("10 / 3")
calculate("5 x 5")
calculate("10 : 2")
calculate("10 / 0")
calculate("abc")
calculate("2 ++")
