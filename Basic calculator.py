v=1
while v==1:
    print("\n            Basic Calculator")

    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the 2nd number: "))

    print("Select the operation you want to perform:")
    print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n ")

    x = int(input("Enter your choice: "))

    match x:
        case 1:
            y = a + b
            print("Sum =", y)

        case 2:
            y = a - b
            print("Sub =", y)

        case 3:
            y = a * b
            print("Mul =", y)

        case 4:
            if b == 0:
                print("Cannot divide by zero")
            else:
                y = a / b
                print("Div =", y)

       

        case _:
            print("Invalid choice")
    
    print("1.Type 1 if you want to continue\n2.Type 0 if you want to exit.")
    v=int(input())
print("Exiting calculator.........")
