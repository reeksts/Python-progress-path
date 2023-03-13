def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet() func inside hello!"

    def welcome():
        return "\t This is the welcome() func inside hello!"

    print("I'm going to return a function")

    if name == "Jose":
        return greet
    else:
        return welcome


greet = hello("Jose")
print(greet())
print(hello())


# Pass function as an argument

def hello():
    return "Hi Jose!"

def other(some_def_func):
    print("Other function runs here")
    print(some_def_func())

other(hello)

print()

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function!")

        original_func()

        print("Some extra code, after the original function!")

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def stuff():
    print("yo yo yo")


stuff()




