x = int
y = "*", '/', '+', '-'
z = int
expression = (input("Expression : "))
if y in ['*', '/', '+', '-']:
    expression = f'{x} {y} {z}'
result = eval(expression)
print(f'{result:.1f}')

    
