#o(1)
def func1(numbers):
    return numbers[0]

# l(log(n))

def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)


func2(10)        