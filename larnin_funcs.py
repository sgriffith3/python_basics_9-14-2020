# Learning Functions

# printing x + 33

def func1():
    print(33)


func1()
print("Let's do that again!")
func1()


def func2(x):
    print(x + 33)


func2(99)
func2(1099)


def func3(y, z):
    print(y * z)


func3(3, 4)


def func4(a, b, c):
    print(a - (b + c))
    return a - (b + c)


def main():
    answer1 = func4(10, 3, 2)
    answer2 = func4(100, 20, 3)
    answer3 = func4(1000, answer1, answer2)
    print(f"The final answer is: {answer3}")


main()

