import time


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def product(x, y):
    return x * y


def division(x, y):
    return x / y


while True:

    print("\nCALCULATOR")
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("Enter Your Choice :")

    user_choice = input()

    if user_choice == "1":
        print("Enter two numbers:")
        x = int(input())
        y = int(input())
        print(f'The sum of the two numbers is {addition(x, y)}')
    elif user_choice == "2":
        print("Enter two numbers:")
        x = int(input())
        y = int(input())
        print(f'The difference of the two numbers is {subtraction(x, y)}')
    elif user_choice == "3":
        print("Enter two numbers:")
        x = int(input())
        y = int(input())
        print(f'The product of the two numbers is {product(x, y)}')
    elif user_choice == "4":
        print("Enter two numbers:")
        x = int(input())
        y = int(input())
        print(f'The quotient of two numbers is {division(x, y)}')
    elif user_choice == "5":
        print("Program is exiting")
        time.sleep(2)
        break
    else:
        print("Invalid Option. Try Again")
        
