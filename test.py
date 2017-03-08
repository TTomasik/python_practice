# # import base64
# # import random
# # import array
# # import struct, binascii
# #
# # with open("/home/tt/workspace/batman.jpeg", "rb") as imageFile:
# #
# #     f = imageFile.read()
# #     print(f)
# #     result=[]
# #     print(bytearray(f))
# #     encoded_string = base64.b64encode(f)
# #     print(encoded_string)
# #     for i in encoded_string:
# #         result.append(i)
# #     print(len(result))
# #     result2 = []
# #     result3 = []
# #     i = 0
# #     new_list = []
# #     while i < len(result):
# #         new_list.append(result[i:i + 3])
# #         i += 3
# #     print(result)
# #     print(new_list)
# #     random.shuffle(new_list)
# #     print(new_list)
# #     for i in new_list:
# #         for k in i:
# #             result2.append(k)
# #     print(result2)
# #     t = bytes(result2)
# #     print(t)
# #
# #
# #     # counter = 0
# #     # for i in result:
# #     #     counter += 1
# #     # print(counter)
# #     #
# #     #
# #     # random.shuffle(result)
# #     # g = bytes(bytearray(result))
# #     # print(f)
# #     # print(g)
# #     # print("-------------")
# #     # result = base64.b64encode()
# #     # result = base64.b64decode(f)
# #     #
# #     # print(result)
# #     g = base64.b64decode(t)
# #     print(g)
# #
# #     # test = bytearray(random.getrandbits(256) for i in result)
# #     # print(test)
# #
# # # print(result)
# # # random.shuffle(result)
# # # print(result)
# # # g = bytearray(result)
# # # print(str(g))
# # fh = open("/home/tt/workspace/imageToSave.jpg", "wb")
# # fh.write(g)
#
# # people = [dict(city="Warsaw", name="Primo", age=28),
# #          {"city": "London", "name": "Luke", "age": 20},
# #          {"city": "Warsaw", "name": "Jaro", "age": 12},
# #          {"city": "New York", "name": "Mike", "age": 40},
# #          {"city": "Cracow", "name": "Adam", "age": 30}]
# #
# # people2 = [{"city": "Warsaw", "name": "Primo", "age": 28},
# #            {"city": "London", "name": "Luke", "age": 20},
# #            {"city": "Warsaw", "name": "Jaro", "age": 12},
# #            {"city": "New York", "name": "Mike", "age": 40},
# #            {"city": "Cracow", "name": "Adam", "age": 30}]
# #
# #
# # # for i in people2:
# # #     print(i)
# #
# # keys = ["city", "name", "age"]
# # values = ["Warsaw", "Primo", 28]
# #
# # people3 = dict(zip(keys, values))
# # for i in [dict(zip(keys, values))]:
# #     print(i["age"])
# #
# # print([dict(zip(keys, values))])
# # test = dict(zip(keys, values))
# # for i in test:
# #     print(i, test[i], sep=": ")
#
# def platform(func):
#     result2=[]
#     def func_to_decorate(numbers):
#         for i in func(numbers):
#             if i % 2 == 0:
#                 result2.append(i)
#         return "Liczby z przedziału: ({}, {}) podzielne przez 3 to: {}, a parzyste i podzielne przez 3 to: {}".format(min(numbers), max(numbers), func(numbers), result2)
#     return func_to_decorate
#
# @platform
# def finder(numbers):
#     result=[]
#     for i in numbers:
#         if i % 3 == 0:
#             result.append(i)
#     return result
#
# print(finder([1,2,3,4,5,6,7,8,9,10]))
#
# class Example(object):
#
#     number = 0
#     @property
#     def number_squared(self):
#         return self.number**2
#
#     @number_squared.setter
#     def number_squared(self, new_number):
#         self.number = [i for i in range(1, new_number+1) if i % 2 == 0]
#
#
#
# ex = Example()
# ex.number = 10
# print(ex.number_squared)
# ex2 = Example()
# ex2.number_squared = 20
# def weird(*args, **kwargs):
#     for i in args:
#         print(i)
#     for i in kwargs:
#         print(i)
#
# weird(1, 2, [0,0,0], "tomek", a='1', b='2', c='3')
#
#
# class A(object):
#     def go(self):
#         print("go A go!")
#     def stop(self):
#         print("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")
#
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print("go B go!")
#
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print("go C go!")
#     def stop(self):
#         super(C, self).stop()
#         print("stop C stop!")
#
# class D(B,C):
#     def go(self):
#         super(D, self).go()
#         print("go D go!")
#     def stop(self):
#         super(D, self).stop()
#         print("stop D stop!")
#     def pause(self):
#         print("wait D wait!")
#
# class E(B,C): pass
#
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
#
# e.stop()
#
#
# # import os
# # def print_directory_contents(sPath):
# #     for sChild in os.listdir(sPath):
# #         sChildPath = os.path.join(sPath,sChild)
# #         if os.path.isdir(sChildPath):
# #             print_directory_contents(sChildPath)
# #         else:
# #             print(sChildPath)
# #
# # print_directory_contents('/home/tt/workspace/tester')
# #
# # print(os.listdir('/home/tt/workspace/tester')[0])
# # print(os.path.join('/home/tt/workspace/tester', os.listdir('/home/tt/workspace/tester')[0]))
#
# class Book(object):
#     name = "Przykład"
#     price = "10zł"
#     author = "Tomasik"
#
#     def __init__(self, n, p, a):
#         print("Tworzę nową książkę")
#         self.name = n
#         self.price = p
#         self.author = a
#
#
#
#     def __repr__(self):
#         return "%s by %s for %s" % (self.name, self.author, self.price)
#
#     def info(self):
#         print("%s by %s for %s" % (self.name, self.author, self.price))
#
#     def question(self, quantity):
#         if self.price * quantity< 100:
#             print("Stać mnie na {}".format(self.name))
#         else:
#             print("Niestety nie stać mnie na {}".format(self.name))
#
#     @staticmethod
#     def class_shouter():
#         print("Wywolales metode na klasie cwianiaczku...")
#
#     @classmethod
#     def class_method(cls):
#         print("Wywolales metode na klasie z jej atrybutami... {}".format(cls.author))
#
# print(Book("tomek", "tomasik", "tom"))
# # book1 = Book("Pani Jeziora", 30, "Andrzej Sapkowski")
# # book2 = Book(n="Pani Jeziora II", p=60, a="Andrzej Sapkowski")
# # book1.info()
# # book1.question(1)
# #
# # Book.class_shouter()
# # Book.class_method()
#
#
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# print("list1 = %s" % list1)
# list2 = extendList(123,[])
# print("list1 = %s" % list1)
# list3 = extendList('a')
# print("list1 = %s" % list1)
#
# class m(dict):
#     def __missing__(self, key):
#         return "kupa"
#
# ex = m()
#
# print(ex["test"])
#
#
# def multipliers():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in multipliers()])
#
# a = [1, "t", "2", True]
# for i in a:
#     if isinstance(i, str):
#         if i.isdecimal():
#             print(i)
#
# def multipliers():
#     for i in range(4):
#         yield lambda x: i*x
#
# for k in multipliers():
#     print(k(2))
#
#
#
#
# #generatory:
# # generator = (i**2 for i in range(4))
# #
# # def generator2():
# #     for i in range(4):
# #         yield i**2
# #
# # for i in generator:
# #     print(i)
# #
# # for i in generator2():
# #     print(i)
#
# #lambdy
# multi_func = lambda x: x*10
# print(multi_func(10))
#
# generator2 = (lambda x: i*x for i in range(4))
#
# for i in generator2:
#     print(i(2))
#
# class DefaultDict(dict):
#     def __missing__(self, key):
#         return []
#
# d = DefaultDict()
#
# d['florp']
# print(d['florp'])
#
# def decorator(func):
#     def wrapper(something):
#         print("printed: '{}' by decorator".format(something))
#     return wrapper
#
# @decorator
# def printer(something):
#     print("printed: '{}' by printer".format(something))
#
# printer("bedzie praca w SAMSUNGU")
#
# # import random
# # def f1(lIn):
# #     l1 = sorted(lIn)
# #     l2 = [i for i in l1 if i<0.5]
# #     return [i*i for i in l2]
# #
# # def f2(lIn):
# #     l1 = [i for i in lIn if i<0.5]
# #     l2 = sorted(l1)
# #     return [i*i for i in l2]
# #
# # def f3(lIn):
# #     l1 = [i*i for i in lIn]
# #     l2 = sorted(l1)
# #     return [i for i in l1 if i<(0.5*0.5)]
# #
# # import cProfile
# # lIn = [random.random() for i in range(100000)]
# # cProfile.run('f1(lIn)')
# # cProfile.run('f2(lIn)')
# # cProfile.run('f3(lIn)')
#
# class Test(object):
#     name = "Jan"
#     surname = "Kowalski"
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @classmethod
#     def info(cls):
#         print("imie tej klasy to {}".format(cls.name))
#
#
#
#
# t = Test("Tomek", "Tomasik")
# print(t.surname)
# Test.info()
#
# class Test2(Test):
#     pass
#
#
# t2 = Test2("Mietek", "Szczesniak")
# print(t2.name)
# import time
# start_time = time.time()
# def fibo_list(n):
#     if n == 0 or n == 1:
#         return n
#     first_two = [0,1]
#     for i in range(2, n):
#         first_two.append(first_two[i-1]+first_two[i-2])
#
#     return first_two[-1]+first_two[-2]
#
# n = 35
# print(fibo_list(n), "list method, time: {}s".format(time.time()-start_time))
#
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fibo(n-1)+fibo(n-2)
#
# n = 35
# print(fibo(n), "recursion method, time: {}s".format(time.time()-start_time))




class Counter(object):

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    @property
    def dynamic_value(self):
        value = self.age*self.weight
        return value


tomek = Counter(30, 90)
print(tomek)



