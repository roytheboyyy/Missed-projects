#Attempt 1
x = int(input("enter your age. Must be between 10 and 20."))
if x > 10 < 20:
    print("Old enough. welcome in!")
else:
    if x == 20 or x == 10:
        print("Just old enough. welcome in!")
    else:
        if x < 10:
            print("Too young. you can't come in")
        else:
            if x > 20:
                print("Too old. you can't come in")
#Attempt 2
x = int(input("enter your age. Must be between 10 and 20."))
if 10 <= x <= 20:
    print("you are in between 10 and 20. welcome in!")
else:
    if x < 10:
        print("Too young. you can't come in")
    else:
        if x > 20:
            print("Too old. you can't come in")