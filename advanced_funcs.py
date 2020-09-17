
def func1(x):
    """
    Accepts the Required Positional Argument x

    Returns the value of x + 25
    """
    return x + 25


def func2(y, z=100):
    """
    Accepts the Required Positional Argument y

    Accepts an Optional Keyword Argument z

    Returns the value of y + z
    """
    return y + z


a = func1(25)
print(a)
print(func2(75))
print(a)
print(func2(a))
print(a)


def func3(b, c=22):
    """
    Accepts the Required Positional Argument b
    
    Accepts the Optional Argument c

    Returns b - c
    """
    return b - c


# def  funcname(<required_positional>, <*args>, <optional/defaulted>):

print(func3(10, c=33))
print(func3(10))


def our_print(*txt):
    print(txt)
    print(type(txt))
    print(txt[0])


our_print("Hi Steve", "Hi Becky", "Hi Bob")
our_print("Hi Bob")


def our_sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(our_sum(1, 2, 3, 4, 5))
print(our_sum(1, 2, 5))


def print_name(fname, lname, mname=None):
    if mname:
        print(fname, mname, lname)
    else:
        print(fname, lname)


print_name("Sam", "Griffith")
print_name(lname="Lane", fname="Bobby")
