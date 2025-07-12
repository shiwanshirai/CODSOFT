def calculate(a,b,o):
    match o:
        case "+":
            s=a+b
            print(f"{a} + {b} = {s}")
        case "-":
            d=a-b
            print(f"{a} - {b} = {d}")
        case "*":
            p=a*b
            print(f"{a} * {b} = {p}")
        case "/":
            q=a/b
            print(f"{a} / {b} = {q}")
while True:
        x=int(input("enter the 1st number: "))
        op=input("enter operator: ")
        y=int(input("enter the 2nd number: "))
        calculate(x,y,op)

        choice = input("Do you want to calculate again? (yes/no): ")
        choice.lower()
        if choice != "yes":
            print("Thanks for using the calculator!")
            break