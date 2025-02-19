# test.py

class MyClass1:
    def __init__(self):
        self.name = "MyClass1"
# ##############################################################################

    def greet(self):
        print(f"Hello from {self.name}!")
# ##############################################################################
# ##############################################################################


class MyClass2:
    def __init__(self, value):
        self.value = value
# ##############################################################################

    def process(self):
        return self.value * 2
# ##############################################################################
# ##############################################################################


def square(x):
    return x ** 2


# ##############################################################################
def cube(x):
    return x ** 3


# ##############################################################################
def main():
    obj1 = MyClass1()
    obj1.greet()

    obj2 = MyClass2(10)
    result = obj2.process()
    print(result)

    num = 5
    squared = square(num)
    print(squared)

    cubed = cube(num)
    print(cubed)


# ##############################################################################
if __name__ == "__main__":
    main()
