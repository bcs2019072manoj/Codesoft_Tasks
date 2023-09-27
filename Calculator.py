'''                            CODSOFT INTERENSHIP
                               
                               
Coder: Manoj kumar
Date: 15/09/2023 to 22/09/2023
Task: 01
Project given by: Codsoft
Interenship
'''

def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        
        next_calculation = input("Let's do next Operation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")