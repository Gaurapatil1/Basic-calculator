def add(x, y):
    return x+y
def sub(x,y):
    return x-y
def multplay(x,y):
    return x*y
def division(x,y):
    if y==0:
      return "Error ! Division by Zero ."
    return x/y
def calculator():
    print("select operation:")
    print("1.Add:")
    print("2.Sub:")
    print("3.Mul:")
    print("4.Div:")

    choice = input("Enter choice (1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(f"result:{add(num1,num2)}")
        elif choice  == '2':
            print(f"result:{sub(num1,num2)}")
        elif choice == '3':
            print(f"result:{multplay(num1,num2)}")
        elif choice == '4':
            print(f"result:{division(num1,num2)}")
        else:
            print("enter valide choice.")
calculator()    
