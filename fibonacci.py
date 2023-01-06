def fibonacci(limit):
    a = 0
    b = 1
    if limit == 0:
        print("invalid")
    elif limit == 1:
        print("0")
    else:
        s = 0
        print("0" + "\n" + "1")
        for i in range(2, limit):
            s = a+b
            a = b
            b = s
            print(b)


fibonacci(int(input("Enter the range :")))
