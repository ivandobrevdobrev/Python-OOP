# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.index = -1
#         self.some_list = [1, 2, 3]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.name)-1:
#             self.index += 1
#             return self.name[self.index]
#         raise StopIteration
#
#
# p = Person("test")
# for obj in p:
#     print(obj)


# Generators

def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n

# Calling teh generator
for el in my_gen():
    print(el)

   #OR
print(list(my_gen())) # will return list [1,2,3]



# Initialize the list
my_list = [1, 3, 6, 10]
# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x**2 for x in my_list])
# the same thing can be done using the generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x**2 for x in my_list))  # синтаксис за правене на генератор
res = ((x**2 for x in my_list))  # за да го извикаме и принтираме го минаваме през For
for el in res:
    print (el)
