import math

a = 0
while a == 0:

    method = input("Write method(-, +, *, / or sqrt = square root, squ = square, sin = math.sin, tan = math.tan, rdg = math.floor)")


    def simple():
        first_number = float(input("Write first number"))
        second_number = float(input("Write second number"))
        if method == "*":
            multiplication = first_number * second_number
            print(multiplication)
        if method == "+":
            multiplication = first_number + second_number
            print(multiplication)
        if method == "/":
            multiplication = first_number / second_number
            print(multiplication)
        if method == "-":
            multiplication = first_number - second_number
            print(multiplication)


    def hard():
        number = float(input("Write number"))
        if method == "sqrt":
            square_root = math.sqrt(number)
            print(square_root)
        if method == "squ":
            square = number * number
            print(square)
        if method == "sin":
            sinus = math.sin(math.radians(number))
            print(sinus)
        if method == "cos":
            cosinus = math.cos(number)
            print(cosinus)
        if method == "tan":
            tg = math.tan(number)
            print(tg)
        if method == "rdg":
            rounding = math.floor(number)
            print(rounding)


    def count():
        if method == "*":
            simple()
        elif method == "+":
            simple()
        elif method == "-":
            simple()
        elif method == "/":
            simple()
        else:
            hard()


    count()
    q = input("If you want continue press YES/ if not press NO")
    if q == "yes":
        a == 0
    elif q == "no":
        a += 1