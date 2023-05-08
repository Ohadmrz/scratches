import math
#
# fil = getfilterby()
# z=[2,3,4,5,6,7,8]
# print(fil(z))     # prints [3,6]

 # def genfilterby2(num):
 #     def inner(ls):
 #         return list(filter(lambda x:x % num == 0,ls))
 #     return inner

#
#
# def getfilterby3(num):
#  return num
# ret_val = getfilterby3(8)
# print(ret_val)

# def geffilterby(num):
#     def inner(ls):
#         ret = []
#         for i in ls:
#             if i % num == 0:
#                 ret.append(i)
#         return ret
#     return inner
#     print(inner)
#
# geffilterby(9)
#
# s = {'orange', 'red', 'green'}
#
# s.add('y')
# print(s)
#
# def convert(s: str, numRows: int) -> str:
#     if numRows == 1:
#         return s
#
#     str_len = len(s)
#     new_str = ""
#
#     diff = 2 * numRows - 2
#
#     for i in range(numRows):
#
#         for j in range(i, str_len, diff):
#             new_str += s[j]
#
#             if (0 < i < numRows - 1) and j + diff - (2 * i ) < str_len:
#                 new_str += s[j + diff - (2 * i)]
#
#     return new_str
#
# print(convert('EBAYISHIRING', 6))
class Cat:
    def __init__(self, cat_type, color, name):
        self.cat_type = cat_type
        self.color = color
        self.name = name

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, dog_type, color, name):
        self.dog_type = dog_type
        self.color = color
        self.name = name

    def make_sound(self):
        print("Wof")


cat = Cat('russian blue', 'grey-blue', 'Oliver')
dog = Dog('doberman', 'black', 'Bruno')

cat.make_sound()
dog.make_sound()
#
# # print(cat.name, dog.name)
#
# animals_list = [cat, dog]
# for animal in animals_list:
#     print(animal.name)
#     animal.make_sound()
