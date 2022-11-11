def func(x, y, *args):
    print(x)
    print(y)
    print(args)
func(1,2,3,4,5)


def func2(x, y):
    print(x)
    print(y)


numbers = {'x':2, 'y':3}
func2(**numbers)


numbers2 = [1,2]

func2(*numbers2)
