#find maximum number in python

def maximum_number(a, b):
    if a>=b:
        return ("first number is maximum", a + "is your maximum number")
    else:
        return ("second number is maximum", b + "is your maximum number")
    

input_a = input("Enter your first number :")
input_b = input("Enter your second number : ")

maximum_number(input_a, input_b)