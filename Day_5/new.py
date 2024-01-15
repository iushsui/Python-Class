a = "Ram"
b = ["kat", "bkt"]
c = [1, 3, [2, 4], 7, 9]
# c[2][1] = 5
c.append("stiring")
# print(type(c))
# print(c)
# print(c[-4])

ab = {
    "x" : 2,
    "y" : "ram"
}
# print(type(ab))
# print(ab["y"])


# x = int(input("Enter number: "))
# print(x)

# list vitra multiple dist - assignment
list_dist = [
    {
        "first_name" : "Ayush",
        "last_name" : "Prajapati"
    },
    {
        "address" : "Thimi",
        "contact" : 9843779904
    },
    "age",
    28
]

print(type(list_dist[1]))


# fstring in print
naam = "Ayush"
age = 28

print(f'My name is {naam}, age {age}')

i = 2
j = "2"
k = i - j # can only multiply (*) int and str, cannot +, -, /
print(k)