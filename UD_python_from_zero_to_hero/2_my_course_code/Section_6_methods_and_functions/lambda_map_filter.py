# MAP FUNCTION:


def square(num):
    return num**2


nums = [1, 2, 3, 4, 5]

# use list on map to get an actual list:
new_list = list(map(square, nums))
print(new_list)
print()

# alternatively, for loop on map will return entries one by one:
for item in map(square, nums):
    print(item)
print()


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))
print()


# FILTER FUNCTION
def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

filtered_list = list(filter(check_even, my_nums))
print(filtered_list)
print()


# LAMBDA EXPRESSIONS:

def square(num):
    result = num**2
    return result


x = 10
# this return only the memory location - not supposed to use lambda in this way.
print(lambda num: num**2)
print()

new_list = list(map(lambda num: num**2, my_nums))
print(new_list)
print()

filtered_list = list(filter(lambda val: val % 2, my_nums))
print(filtered_list)
print()

for i in my_nums:
    print(i % 2)
print()

chars = list(map(lambda name: name[0], names))
print(chars)

