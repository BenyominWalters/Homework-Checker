#Homework Checker I made for my son
#learning less than, greater than, and equal to.

while True:
    print("~~~~~ The Incredible Homework Checker ~~~~~~\n")

    x = float(input("What is your first number? "))
    print("Your first number is", x, "\n")
    y = float(input("What is your second number? "))
    print("Your second number is", y, "\n")

    if x==y:
        print(x, "is equal to", y, "\n")
    elif x > y:
        print (x, "is greater than", y, "\n")
    else:
        print (x, "is less than", y, "\n")

    print("Did you get it right? \n")
          
