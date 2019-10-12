def addition(x, y):
    outcome = x+y
    print(str(x) + "+" + str(y) + "=" + str(outcome))


def begin():

    operation_chosen = str(input("What operation would you like to use? "))
    x = int(input("What number do you want to use? "))
    y = int(input("choose another number "))

    if (operation_chosen == "addition"):

        addition(x, y)


begin()
