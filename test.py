# import base64
# import random
# import array
# import struct, binascii
#
# with open("/home/tt/workspace/batman.jpeg", "rb") as imageFile:
#
#     f = imageFile.read()
#     print(f)
#     result=[]
#     print(bytearray(f))
#     encoded_string = base64.b64encode(f)
#     print(encoded_string)
#     for i in encoded_string:
#         result.append(i)
#     print(len(result))
#     result2 = []
#     result3 = []
#     i = 0
#     new_list = []
#     while i < len(result):
#         new_list.append(result[i:i + 3])
#         i += 3
#     print(result)
#     print(new_list)
#     random.shuffle(new_list)
#     print(new_list)
#     for i in new_list:
#         for k in i:
#             result2.append(k)
#     print(result2)
#     t = bytes(result2)
#     print(t)
#
#
#     # counter = 0
#     # for i in result:
#     #     counter += 1
#     # print(counter)
#     #
#     #
#     # random.shuffle(result)
#     # g = bytes(bytearray(result))
#     # print(f)
#     # print(g)
#     # print("-------------")
#     # result = base64.b64encode()
#     # result = base64.b64decode(f)
#     #
#     # print(result)
#     g = base64.b64decode(t)
#     print(g)
#
#     # test = bytearray(random.getrandbits(256) for i in result)
#     # print(test)
#
# # print(result)
# # random.shuffle(result)
# # print(result)
# # g = bytearray(result)
# # print(str(g))
# fh = open("/home/tt/workspace/imageToSave.jpg", "wb")
# fh.write(g)

# people = [dict(city="Warsaw", name="Primo", age=28),
#          {"city": "London", "name": "Luke", "age": 20},
#          {"city": "Warsaw", "name": "Jaro", "age": 12},
#          {"city": "New York", "name": "Mike", "age": 40},
#          {"city": "Cracow", "name": "Adam", "age": 30}]
#
# people2 = [{"city": "Warsaw", "name": "Primo", "age": 28},
#            {"city": "London", "name": "Luke", "age": 20},
#            {"city": "Warsaw", "name": "Jaro", "age": 12},
#            {"city": "New York", "name": "Mike", "age": 40},
#            {"city": "Cracow", "name": "Adam", "age": 30}]
#
#
# # for i in people2:
# #     print(i)
#
# keys = ["city", "name", "age"]
# values = ["Warsaw", "Primo", 28]
#
# people3 = dict(zip(keys, values))
# for i in [dict(zip(keys, values))]:
#     print(i["age"])
#
# print([dict(zip(keys, values))])
# test = dict(zip(keys, values))
# for i in test:
#     print(i, test[i], sep=": ")

def platform(func):
    result2=[]
    def func_to_decorate(numbers):
        for i in func(numbers):
            if i % 2 == 0:
                result2.append(i)
        return "Liczby z przedziału: ({}, {}) podzielne przez 3 to: {}, a parzyste i podzielne przez 3 to: {}".format(min(numbers), max(numbers), func(numbers), result2)
    return func_to_decorate

@platform
def finder(numbers):
    result=[]
    for i in numbers:
        if i % 3 == 0:
            result.append(i)
    return result

print(finder([1,2,3,4,5,6,7,8,9,10]))

class Example(object):

    number = 0
    @property
    def number_squared(self):
        return self.number**2

    @number_squared.setter
    def number_squared(self, new_number):
        self.number = [i for i in range(1, new_number+1) if i % 2 == 0]



ex = Example()
ex.number = 10
print(ex.number_squared)
ex2 = Example()
ex2.number_squared = 20
def weird(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs:
        print(i)

weird(1, 2, [0,0,0], "tomek", a='1', b='2', c='3')


class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()


def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

