# a = 10
# b = 30
# c = 50

# if a > b and a > c:
#     print("A is biggest among a, b, c")
# elif b > a and b > c:
#     print("B is biggest")
# elif c > a and c > b:
#     print("C is biggest")
# else:
#     print("All are equal")


## Create a function

def Check_biggest(a, b, c):
    
    if a > b and a > c:
        print("A is biggest among a, b, c")
    elif b > a and b > c:
        print("B is biggest")
    elif c > a and c > b:
        print("C is biggest")
    else:
        print("All are equal")



# Check_biggest(10, 20, 30)
# Check_biggest(10, 20, 30)
# Check_biggest(10, 20, 30)
# Check_biggest(10, 20, 30)
# Check_biggest(10, 20, 30)

for i in range(1,6):
    Check_biggest(10, 20, 30)