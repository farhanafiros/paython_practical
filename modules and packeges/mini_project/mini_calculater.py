def calculater():
    try:
        a = float(input("enter first number"))
        b = float(input("enter second number"))
        op = input("Enter oprater(+,-,*,/)")

        if op =='+': 
            print("result:", a + b)
        elif op =='-':
            print("result:" ,a - b)
        elif op =='*':
            print("result:", a * b)
        elif op =='/':
            print ("result:", a / b)
        else:
            raise ValueError("invalied operator")
    
    except ValueError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: division by zero not allowed")

    finally: 
        print("Thank you for using the calculator.")
calculater()



