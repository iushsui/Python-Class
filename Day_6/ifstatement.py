p = float(input("Enter your percentage: "))

if (p > 100):
    print("Invalid percetage")
else:
    if (p >= 80):
        print('Distinction')
    elif (p >= 60.00) and (p <= 79.99):
        print('1st Division')
    elif (p >= 40.00) and (p <= 59.99):
        print('2nd Division')
    else:
        print('Fail')
    