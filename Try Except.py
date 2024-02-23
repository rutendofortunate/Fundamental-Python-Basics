


try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
#don't just use except without a specific error because its just too broad
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")