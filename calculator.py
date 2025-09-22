#!/usr/bin/env python3
"""
Simple Calculator CLI
- functions for each operation
- uses input()
- loops until user chooses to exit
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            val = float(s)
            return val
        except ValueError:
            print("Invalid number. Please enter a numeric value (e.g. 3.5 or 10).")

def show_menu():
    print("\nSimple Calculator")
    print("1) Add (+)")
    print("2) Subtract (-)")
    print("3) Multiply (*)")
    print("4) Divide (/)")
    print("5) Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '5':
            print("Goodbye!")
            break
        if choice not in {'1','2','3','4'}:
            print("Invalid choice. Pick 1,2,3,4 or 5.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if choice == '1':
                res = add(a,b)
                op = '+'
            elif choice == '2':
                res = sub(a,b)
                op = '-'
            elif choice == '3':
                res = mul(a,b)
                op = '*'
            elif choice == '4':
                res = div(a,b)
                op = '/'
            print(f"\nResult: {a} {op} {b} = {res}\n")
        except ZeroDivisionError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
