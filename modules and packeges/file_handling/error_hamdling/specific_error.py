try :
    number = int(input("enter a number:" ))
    result = 10 / number
    print (result)
except ValueError: 
    print("Enter a valied number")
except ZeroDivisionError:
    print("cannot divide by ZeroDivisionError")
      