# a = "test"
# b = "test"
# print(a)

# if a == b:
#     print("pass")

# # nested if
# if a > b:
#     print("test pass")
# elif (a == b):
#     print("eaual pass")
#     if isinstance(123, int):
#         print("datatype pass")
#     elif (a < b):
#         print("opeartor pass")
# else:
#     print("whole program fail")


# # one line if condition
# gender = "m"
# data = "Male" if gender == 'M' else "Female"
# print(data)

# PSEUDO CODE
# 1 input, total sales - type casting (always at int)
# thereshold sale(target sales) = 3000
# 3000 to 4000 - 2% commission
# 4000 to 5000 - 5% commision
# 5000 upto 10% commission
# no commission

total_sales = int(input("Enter total sales: "))
target_sales = 3000

if (total_sales >= target_sales):
    if (total_sales >= 3000) and (total_sales < 4000) :
        print(f'Commission is 2%')
    elif (total_sales >= 4000) and (total_sales < 5000) :
        print(f'Commission is 5%')
    elif (total_sales >= 5000) :
        print(f'Commission is 10%')
    else :
        print(f'No commission')
else :
    print(f'Sorry, you did not meet your target')
