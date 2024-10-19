# defining a function to calculate HCF
def calculate_hcf(x, y):
    # selecting the smaller number
    if x > y:
        greater= x
    else:
        greater = y
    while True:
       if ((greater % x == 0) and (greater% y == 0)):
            lcm=greater
            break
       greater+=1
    return lcm


# taking input from users
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The H.C.F. of", num1, "and", num2, "is", calculate_hcf(num1, num2))