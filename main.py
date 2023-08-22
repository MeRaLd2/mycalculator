def add(x, y):
    return x + y

print("Select operation:")
print("1. Add")

choice = input("Enter choice (1): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
else:
    print("Invalid input")