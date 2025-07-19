# # syntax - lambda arguments: expression

# # def add(a, b):
# #     return a+b

# res = lambda a,b: a+b
# sum = res(10,20)
# print(sum)

# # square of number

# square = lambda x: x*x
# print(square(5))

# map()

# nums = [1,2,3,4,5]
# square = list(map(lambda x: x*x, nums))
# print(square)

# filter()

# nums = [1,2,3,4,5]
# evens = list(filter(lambda x: x%2 == 0, nums))
# print(evens)

# sorted()

# students = [('name1', 88), ('name2', 89), ('name3', 45), ('name4', 78)]
# sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

# print(sorted_students)