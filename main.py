# Python Program to find Factors of a Number using Functions #

def find_factors(number):
    for value in range(1,number + 1):
        if (number% value == 0):
            print("{0}",format(value))

number = int(input("Please enter the number:"))
print("Factors of Given Number {0} are:", format(number))
find_factors(number)

