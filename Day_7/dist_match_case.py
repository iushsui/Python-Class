choice = int(input(
    "Enter number for operation \n"
    "1: Addition \n"
    "2: Substraction \n"
))

if choice ==  1 :
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a+b)
elif choice == 2:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a-b)
else :
    print("Invalid choice")





dist = {
    "add" : 1,
    "sub" : 2
}
