# # hint, to convert string to number use
# variable_name = "23"
# num1 = int(variable_name)

# str = input("what is your number: ")
# numb = int(str)

x = input("type a number: ")
y = input("type another number: ")
z = int(x) + int(y)
if z>10:
    print("greater than 10")
elif z<10:
    print("less than 10")
else:
    print("sum is 10, correct")
    