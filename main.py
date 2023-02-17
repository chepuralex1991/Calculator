from calculator.converter import from_base, to_base
from calculator.evaluation import evaluate
try:
    base = int(input('Enter the base (2-62): '))
    if base not in [2, 8, 10, 16, 36]:
        print("Invalid input. Please enter a valid base (2, 8, 10, 16, 36, 62).")
        exit()
    x = input('Enter first number: ')
    y = input('Enter second number: ')
except ValueError as e:
    print(f"It's not an integer")
    exit()

print("""Select operation: 
1. Add
2. Substract
3. Multiply
4. Divide""")
choice = int(input('Choose the option:'))
x_dec = from_base(x, base)
y_dec = from_base(y, base)

result_dec = evaluate(x_dec, y_dec, choice)

result_base = to_base(result_dec, base)
try:
   print(result_base)
except (TypeError, ZeroDivisionError) as e:
    print("Something bad happened!", e)
    exit()