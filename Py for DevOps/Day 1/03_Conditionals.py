a = 10
b = 30
c = 50

# if a > b:
#     print("A is bigger")
# else:
#     print("B is bigger")



# env = "dev"
# # env = "prod" # or prd

# if env == "dev":
#     print("Yes this is")
# else:
#     print("No, it's not")



if a > b and a > c:
    print("A is biggest among a, b, c")
elif b > a and b > c:
    print("B is biggest")
elif c > a and c > b:
    print("C is biggest")
else:
    print("All are equal")
