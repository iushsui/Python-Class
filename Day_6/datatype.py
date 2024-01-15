# # boolean
# a = True
# b = False

# x = 2
# y = 4
# print(type(x>y))

a = input("Enter user name: ")
b = input("Enter contact: ")
c = input("Enter age: ")

user_info = []

user_info.append(a)
user_info.append(b)
user_info.append(c)

dist = {}
dist["last_name"] = input("Enter last name: ")
dist["address"] = input("Enter address: ")
dist["dob"] = input("Enter dob: ")

user_info.append(dist)

# user_info.append(dist)

print(f'List: Name is {user_info[0]}, contact number is {user_info[1]} age is {user_info[2]}')
print(f'Dictionary: {dist}')
print(f'Appending dist: {user_info}' )
