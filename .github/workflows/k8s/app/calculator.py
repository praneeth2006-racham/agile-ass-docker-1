def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def menu():
    print("\n--- Calculator Menu (Push 1) ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice (1-3): ")
        if choice == '3':
            print("Exiting...")
            break
        if choice in ('1', '2'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numbers.")
        else:
            print("Invalid choice!")
