def divide(dividend, divisor):
    #if divisor == 0:
    #   raise ZeroDivisionError("Divisor cannot be 000.")
        
    return dividend / divisor


grades = []

print("Welcom to teh average grade program.")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades to print")
except ValueError:
    print("tatataaa")
else:
    print(f"The average grade is {average}.")
finally:
    print("sss")
