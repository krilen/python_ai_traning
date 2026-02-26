
def fib(num: int =0, x: int =0, y: int =1 ) -> None:
    if num == 0:
        print()
        return 
    
    else:
        print(x, end=", ")

        fib(num -1, y, x +y)


fib(7)
fib(12)
fib(0)
fib(1)
fib(2)
