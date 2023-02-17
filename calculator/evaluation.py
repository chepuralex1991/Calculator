def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def evaluate (x,y,choice):
    result_1 = None
    try:
        if choice == 1:
            result_1 = x + y

        elif choice == 2:
            result_1 = x - y

        elif choice == 3:
            result_1 = x * y

        elif choice == 4:
            result_1 = x / y
        return result_1
    except (TypeError, ZeroDivisionError) as e:
        print("Something bad happened!", e)
        exit()