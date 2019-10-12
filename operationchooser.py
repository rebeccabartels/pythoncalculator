

def addition(x, y):
    outcome = x+y
    print(str(x) + "+" + str(y) + "=" + str(outcome))


def begin():

    operation_chosen = str(input(
        "What operation would you like to use? \n[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Division\nEnter Choice: "))
    x = int(input("Choose a number "))
    y = int(input("Choose another number "))

    if (operation_chosen == "[1]"):

        addition(x, y)


begin()
