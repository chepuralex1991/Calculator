from Calculator.evaluation  import evaluate

def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


x = input('Enter first number: ')
y = input('Enter second number: ')
print("""Select operation: 
1. Add
2. Substract
3. Multiply
4. Divide""")
choice = int(input('Choose the option:'))

evaluate(x,y,choice)
print(evaluate(x,y,choice))
