u_choice=True
while u_choice:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operator=input("enter the operator(+,-,*,/): ")
    match operator:
        case "+":
            print(num1+num2)
        case "-":
            print(num1-num2)
        case "*":
            print(num1*num2)
        case "/":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(num1/num2)
        case _:
            print("Invalid operator")
    u_choice=input("Do you want to continue?(y/n): ").lower()=='y'