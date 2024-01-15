# fruits = ["mango", "orange", "banana"]
# # fruits.append("apple")
# fruits.extend(["apple", "cherry"])
# for x in fruits:
#     if x == "orange" or "apple":
#         continue
#     print(x)
#     # print(type(x))


# # for x in "boradway":
# #     print("\n", x)

# dist = {
#     "name": "Aush",
#     "age": 22
# }

# # print(type(dist))

# # for x in dist:
# #     # if dist['age'] == 22:
# #     #     break
# #     print(f'{x} :{dist[x]}')


# checklist = ["Ram", 2, 2.0 ]
# for items in checklist:
#     if isinstance(items, int):
#         continue
#     print(items)

# x = int(input("Which number's table you wanna genrate? "))
# for i in range(1, 11, 1) :
#     multiply = x * i
#     print(f'{x} x {i} = {multiply}')


# # 1 to 5 muliple, store 1 to 5 in a list, and generate their tables - ASSIGNMENT
# list = [1, 2, 3, 4, 5]
# # for i in range(1,11):
#     # print(i)
# for x in list:
#     for i in range(1,11):
#         print(f'{x} x {i} = {x * i}')
#     print('\n')


l = []
r = int(input("How many numbers of table you want to generate? "))
if r > 5:
    print("Values should not be greater than 5")
else: 
    for m in range(1,r+1):
        n = int(input("Enter number to get table: "))
        l.append(n)
        # print(l)
        for x in l:
            for i in range(1,11):
                print(f'{x} x {i} = {x * i}')
            print('\n')

    