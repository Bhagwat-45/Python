def fib(int1:int):
    if int1<=0:
        return 0
    elif int1==1:
        return 1
    else:
        return fib(int1-1)+fib(int1-2)

print(fib(23))