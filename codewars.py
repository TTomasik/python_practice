import math
from subprocess import list2cmdline
import time

# #---EX1 -> finds two smallest integers and show sum of them
# numbers = [1, 10, 22, 4]
# def sum_two_smallest_numbers(numbers):
#          
#     
#     print(numbers)
#     numbers.sort()
#     print(numbers)
#     result = numbers[0]+numbers[1]
#     print(result)
#     return result
#    
# 
# sum_two_smallest_numbers(numbers)

# #---EX2 -> squares every single integer and join int to one integer at the end
# num = 123
# str(num)
# list = []
# result = []
# def haha(liczby):
#     for a in str(num):     
#         b = int(a)**2
#         list.append(b)
#     return ''.join(str(x) for x in list)  
#         
# print(haha(num))

# #---EX3 -> makes first letter capital    
# quote = "cant wait till summer"
# def capital(quotes):
#     list = quotes.split()    
#     result = []
#     for word in list:               
#         result.append(word[0].upper()+word[1:])        
#     return " ".join(result)
# 
# print(capital(quote))
# 
# print(quote.title()) # this one line does the same that the whole function above
    
# #---EX4 -> makes sum from range    
# def get_sum(a,b):
#     if a < b:
#         return sum(list(range(a,b+1)))
#     elif a > b: 
#         return sum(list(range(b,a+1)))
#     elif a == b:
#         return a  
# 
# print(get_sum(2,2)) 

# #---EX5 -> hard camel case
# def accum(s):
#     result = []
#     for index, x in enumerate(s):
#         x = x.upper() + x.lower()*len(s[:index])
#         result.append(x)
#     return "-".join(result)   
# 
#     
# string = "sfbjASFASDVNkxncv"
# print(accum(string))

# #---EX6 -> finding how many times number appear in array and check if number of appears %2!=0
# def find_it(seq):    
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i                     
#                    
# example = [20, 2, 2, 11, 11, 12, 13, 1, 2, 11, 11]
# print(find_it(example))
               
# #---EX7 -> give three dimensions and check if you can build a triangle from them
# def is_triangle(a, b, c):
#     if a+b>c and a+c>b and b+c>a:
#         return True
#     else:
#         return False

# #---EX8 -> You are given an array strarr of strings and an integer k. 
# #           Your task is to return the first longest string consisting of k consecutive strings
# #           taken in the array.
# def longest_consec(starr, k):
#     result=[]
#     if k <= 0 or k > len(starr) or len(starr) == 0:        
#         return ""
#     else:
#         for i in range(0, len(starr), 1):
#             result.append("".join(starr[i:i+k]))        
#     return max(result, key=len)
#  
# starr = ["zone", "abigail", "theta", "form", "libe", "zas"]
# k = 2
# print(longest_consec(starr, k))

# #---EX9 -> quadratic equation
# def find_nb(m):
#     delta = 1 + 4*(2*math.sqrt(m))
#     if delta > 0:
#         x_1 = (-1 - math.sqrt(delta))/2
#         x_2 = (-1 + math.sqrt(delta))/2     
#         if x_1 > x_2 and x_1%1 == 0:                        
#             return int(x_1)
#         elif x_1 < x_2 and x_2%1 == 0:
#             return int(x_2)
#         else:
#             return -1     
#     elif delta < 0:
#         return -1       
# 
# print(find_nb(450010))

# #---EX10 -> decoder, key word = WUB
# def song_decoder(song):
#     splited = song.split("WUB")
#     result = []
#     if splited[0] == "":        
#         splited.remove("")
#     for w in splited:
#         if w != "":
#             result.append(w)
#     return " ".join(result)
#  
# example = "WUBTOWUBWUBWUBWUBJAWUBTOMEK"            
# print(song_decoder(example))

# #---EX11 -> remove smallest, only one digit, dont mutate the array
# def remove_smallest(numbers):
#     if len(numbers) == 0:
#         return []
#     else:
#         numbers.remove(sorted(numbers)[0])
#         return numbers
# 
# ex = [1]
# example = [5, 4, 2, 8, 9, 1, 1, 1]
# print(remove_smallest(ex)) 
    
# #---EX12 -> return middle string or pair of strings
# def get_middle(s):
#     if len(s)%2 == 0:
#         middle = int(len(s)/2-1)        
#         return s[middle:middle+2]
#     else:
#         middle = int(len(s)/2)
#         return s[middle]
# 
# ex1 = "ttEStt"
# ex2 = "a"
# print(get_middle(ex2))

# EX13 --> convert sum of two digits into binary - MY SOLUTION - I DIDNT FINISH IT
#  def add_binary(a,b):
#      binary = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8]
#      sum_a_b = a + b
#      result = []
#      print(sum_a_b-1)
#      if sum_a_b % 2 == 0:
#          for index, x in enumerate(binary):
#              if x == sum_a_b:
#                  print(index, x)
#                  for i in range(0, index):
#                      result.append(0)
#                  result.append(1)
#                  result.reverse()
#                  return ''.join(str(k) for k in result)
#              else: 
#                  sort = sorted(binary)
#                  binary.append(sum_a_b)
#                  for i, k in enumerate(sort):
#                      if k == sum_a_b:
#                          print(sort[i]-sort[i-1])
#                          if sort[i]-sort[i-1]
#                          return(i, k, sort)
# 
# #---EX13 --> simplest solution      
# def add_binary(a,b):
#     sum_a_b = a + b
#     return "{0:b}".format(sum_a_b)  
#     
# 
# a = 2
# b = 32
# print(add_binary(a,b))

# #---EX14 -> sum of left side of index equal sum of right side of index and return index
# def find_even_index(arr):
#     a = 0
#     b = 0
#     result = []
#     reverse_result = []
#     final = []
#     reversed = arr[::-1]    
#     for x in arr:               
#         a += x
#         result.append(a)      
#     for y in reversed:
#         b += y
#         reverse_result.append(b)
#     for (x1, x2) in zip(result, reverse_result[::-1]):
#         c = x1 - x2
#         final.append(c)  
#     for index, z in enumerate(final):
#         if 0 not in final:
#             return -1
#         else:
#             if z == 0:
#                 return index
# 
# arr = [100, 1, 1, 9, 20, 20, 50]
# 
# print(find_even_index(arr))

# #---EX14 -> BETTER SOLUTION :)
# def find_even_index(lst):
#     left_sum = 0
#     right_sum = sum(lst)
#     for i, a in enumerate(lst):
#         right_sum -= a
#         if left_sum == right_sum:
#             return i
#         left_sum += a
#     return -1

# #---EX14 -> THE BEST SOLUTION!!!
# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1

# #---EX15 -> find numbers in list that number % 3 or number % 5 == 0, then make sum of them
# def solution(number):
#     result = []
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             result.append(i)
#     return(sum(result))          
#  
# number = 10
# print(solution(number))

# def longest_palindrome(s):    # I HAVENT FINISH IT
#     for i in list(s):
#         if i == i+1:
#              
#             if i-1 == i+2:
#                 if i-2 == i+3:
#                     pass
#             else:
#             return(i, i+1)
#                 return(i-1, i, i+1, i+2)
#                     return(i-2, i-1, i, i+1, i+2, i+3)
#      
#      
#  
# s = 'baablkj12345432133d'
# print(longest_palindrome(s)) 

# #---EX16
# def narcissistic(value):    
#     int_list = [int(x) for x in str(value)]
#     result=[]
#     for i in int_list:
#         i**=(len(int_list))
#         result.append(i)
#     if sum(result) == value:
#         return True
#     else:
#         return False      
# 
# value = 153
# print(narcissistic(value))

# #---CODILITY1
# def solution(N):
#     N = "{0:b}".format(N)
#     print(N)
#     result = []
#     counter = 0
#     if "0" in str(N):
#         for i in str(N):
#             if i == "1":            
#                 result.append(counter)
#                 counter = 0            
#             if i == "0":
#                 counter += 1
#         return max(result)
#     else:
#         return 0
#         
# 
# N=256
# print(solution(N))
# #---CODILITY2 
# def solution(A):
#     result = []
#     for i in range(1, 1000001, 2):
#         counter = A.count(i)
#         if counter % 2 != 0:
#             return i
#         
#     
#     
# A=[9, 9, 1, 1, 1, 0, 0]
# print(solution(A))  

# #---CODILITY3
# def solution(A, K):
#     for i in range(K):
#         A.insert(0,A.pop())
#     return A
#
#
# K=2
# A=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(solution(A, K))

# #---CODILITY4
# import math
# def solution(X, Y, D):
#     if X == Y:
#         return 0
#     else:        
#         range_xy = Y-X        
#         jumps = math.ceil(float(range_xy)/D)    #float - becouse of python 2.7        
#         return int(jumps)                       #int - becouse of python 2.7
# 
# X = 10
# Y = 85
# D = 30
# print(solution(X, Y, D))
# #---CODILITY5
# def solution(A):
#     if len(A) == 0:
#         return 1
#     elif len(A) == 1:
#         return 1
#     for index, i in enumerate(sorted(A)):
#         if sorted(A)[index] != sorted(A)[index+1]-1:
#             return(i+1)
#             
#             
# 
# 
# A = [9, 7]
# print(solution(A))
# #---FIBONACCI
# def fibonacci(n):
#     numbers = [0, 1]
#     for i in range(2,n):
#         numbers.append(numbers[i-1]+numbers[i-2])
#     return numbers, sum(numbers)
#
# n = 50
# print(fibonacci(n))

# #---EX17
# def cakes(r, a):
#     list = []
#     list_available = []
#     list_recipe = []  
#     if len(a) < len(r):
#         return 0
#     else:        
#         for k in a.keys() & r.keys():            
#             list_available.append(a[k])
#             list_recipe.append(r[k])
#         result = [x1 / x2 for (x1, x2) in zip(list_available, list_recipe)]      
#     return int(min(result))
#     
# 
# r = {'flour': 500, 'sugar': 200, 'eggs': 1}
# a = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(r, a))

# #---EX17 -> better solution
# def cakes(recipe, available):
#     args = []
#     for k in recipe.keys():
#         if k not in available:
#             return 0
#         args.append(available[k] //recipe[k])
#     return min(args)

# #---EX18 -> hard exercise -> problems with False, 0.0 and 0
# def move_zeros(array):
#     counter = array.count(0)    
#     for x in array:
#         if x is False:
#             counter -= 1   
#     return [x for x in array if x is not 0 and not isinstance(x, float)] + [0]*counter
# 
# 
# array = [None, False, 9, [], 0, 0, 0.0, 1, 2, 0, 5]
# print(move_zeros(array))

# #---CODILITY6
# def solution(A):
#     if len(A) <= 1:
#         return 0
#     else:
#         sum_left = A[0]
#         sum_right = sum(A)-A[0]    
#         list_left = [sum_left]
#         list_right = [sum_right]    
#         for i in range(1, len(A)-1):
#             sum_left += A[i]
#             sum_right -= A[i]
#             list_left.append(sum_left)
#             list_right.append(sum_right)
#         return min([abs(x1 - x2) for x1, x2 in zip(list_left, list_right)])
# 
# A = [6]
# print(solution(A))

# #---CODILITY7
# def solution(A):       
#     if len(A) == 0:
#         return 0 
#     if len(A) == 1:
#         return A[0]   
#     sorted_A = sorted(A)
#     print(sorted(A))    
#     for i in range(len(sorted_A)-1):             
#         if sorted_A[i]+1 < sorted_A[i+1]:
#             result = sorted_A[i]+1          
#     return result    
#         
# 
# A = [333]
# print(solution(A))
    
# #CODILITY-8    
# def solution(X, A):
#     if A.count(X) == 0:
#         return -1
#     else:
#         for index, i in enumerate(A):
#             if i == X:
#                 return index
#         
# 
# X = 11
# A = [1, 3, 1, 4, 2, 3, 5, 4]
# print(solution(X, A))  

# #CODILITY9
# def solution(A):
#     if len(A) <= 1:
#         return 0
#     else:         
#         for i in A:
#             if A.count(i) > 1:
#                 return 0                  
#         sort_A = sorted(A)
#         comparator = list(range(min(A), max(A)+1))
#         difference = [x1 - x2 for x1, x2 in zip(comparator, sort_A)]
#         if all(i == 0 for i in difference):
#             return 1
#         else:
#             return 0  
# 
# A = [1, 3]
# print(solution(A))
    
# #CODILITY10   
# def solution(N, A):
#     proper = []
#     array = [0]*N
#     for i in A:
#         i -= 1
#         proper.append(i)
#     for i in proper:
#         if i >= 0:            
#             if i <= len(array)-1:
#                 array[i] += 1                                                       
#             if i == len(array):
#                 b = max(array)            
#                 array = [b]*N
#         else:
#             pass
#     return array        
# 
# N=5
# A=[3, 4, 4, 6, 1, 4, 4]
# 
# print(solution(N, A))

# #CODILITY11
# def solution(A, B, K):    
#     if A == B:
#         if A%K == 0:
#             return 1
#         else:
#             return 0
#     if K != 0 and A < B and A > 0 and B > 0:
#         result = []
#         for i in range(A, B+1):    #in python 2.7 it should be xrange
#             if i%K == 0:
#                 result.append(i)
#         return len(result), result
#     else:
#         return 0
#     
#     
# A = 10
# B = 20
# K = 2  
# print(solution(A, B, K))

# #CODILITY12
# def solution(S, P, Q):
#     if max(P) > len(S)-1 or max(Q) > len(S)-1:
#         return False
#     A, C, G, T = 1, 2, 3, 4
#     dna = []
#     result = [[] for x in range(len(P))]    
#     for index, i in enumerate(P):
#         for k in Q:
#             a_min = i
#             a_max = Q[index]+1
#             code = S[a_min:a_max]
#             dna.append(code)
#     for index, i in enumerate(dna[::3]):               
#         for x in list(i):            
#             if x == "A":
#                 result[index].append(ord(x)-64)
#             if x == "C":
#                 result[index].append(ord(x)-65)
#             if x == "G":
#                 result[index].append(ord(x)-68)
#             if x == "T":
#                 result[index].append(ord(x)-80) 
#     answer = []
#     for y in result:
#         answer.append(min(y))
#     return answer     
# 
# S = 'CAGCCTA'
# P = [2, 5, 0]
# Q = [4, 5, 6]
# print(solution(S, P, Q))

# #EX---19
# def longest_slide_down(pyramid):
#     result = [pyramid[0][0]]
#     result_alternative = [pyramid[0][0]]
#     indexes = [0]
#     for j, i in enumerate(pyramid):                
#         a = max(i[indexes[j]:indexes[j]+2])
#         b = min(i[indexes[j]:indexes[j]+2])
#         result.append(a)
#         result_alternative.append(b)
#         if sum(result[-1:-3:-1]) < sum(result_alternative[-1:-3:-1]):
#             result[-1] = result_alternative[-1]
#             result[-2] = result_alternative[-2]            
#         for k, l in enumerate(i):            
#             if l == a and len(i[0:k]) >= indexes[j]:                
#                 indexes.append(k)
#     return sum(result[1::]), result, result_alternative, indexes
# 
# 
# pyramid =   [[75],
#             [95, 64],
#             [17, 47, 82],
#             [18, 35, 87, 10],
#             [20,  4, 82, 47, 65],
#             [19,  1, 23, 75,  3, 34],
#             [88,  2, 77, 73,  7, 63, 67],
#             [99, 65,  4, 28,  6, 16, 70, 92],
#             [41, 41, 26, 56, 83, 40, 80, 70, 33],
#             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#             [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#             [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
# print(longest_slide_down(pyramid))

# #EX---20
# def rot13(message):
#     input = []
#     output = []
#     result = []
#     for i in message:
#         input.append(ord(i))
#     for k in input:
#         if k in range(97, 123):
#             a = k+13
#             if a > 122:
#                 a_new = 97 + (a - 123)
#                 output.append(a_new)
#             else:
#                 output.append(a)
#         if k in range(65, 91):
#             a = k+13
#             if a > 90:
#                 a_new = 65 + (a - 91)
#                 output.append(a_new)
#             else:
#                 output.append(a)
#         if k not in range(97, 123) and k not in range(65, 91):
#             output.append(k)
#     for j in output:
#         result.append(chr(j))
#     return "".join(result)
#
# message = "12412///1Test"
# print(rot13(message))

# #EX---21
# import re
# def domain_name(url):
#     if "www" in url:
#         result = re.search(r'(?<=www.)\w+(\-\w+)?', url)
#     if "www" not in url:
#         result = re.search(r'(?<=//)\w+(\-\w+)?', url)
#     return result.group(0)
#
# url = "www.bites.com"
# print(domain_name(url))

# #EX---22
# def simplify(poly):
#     result = []
#     str_int = []
#     result_joined = []
#     result_joined_sorted = []
#     for i in poly:
#         result.append(i)
#     for index, k in enumerate(result):
#         if ord(k) in range(97, 123) or ord(k) in range(49, 58):
#             str_int.append(k)
#             if index == len(result) - 1:
#                 joined = "".join(str_int)
#                 result_joined.append(joined)
#         else:
#             joined = "".join(str_int)
#             result_joined.append(joined)
#             result_joined.append(k)
#             str_int = []
#     for i in result_joined:
#         result_joined_sorted.append("".join(sorted(i)))
#
#
#
#     return result, result_joined_sorted
#
# poly="3ab+ba-4ac+12ca"
# print(simplify(poly))

# def tester(poly):
#     for i in poly:
#         if int(i):
#
#
# poly = "3ab+ba-4ac+12ca"
# print(tester(poly))
import math
# #EX---23
# def whoIsNext(names, r):
#     counter=2
#     if r <= 1000000000:
#         for i in range(0, r):
#             if i % 5 == 0 and i is not 0:
#                 counter*=2
#                 del names[0:i]
#             names.extend([names[i]]*counter)
#         return names[-1], names
#     pass
#
#
# names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
# r = 7
# print(whoIsNext(names, r))

# #EX---24
# def josephus(items, k):
#     k -= 1  # pop automatically skips the dead guy
#     idx = k
#     result = []
#     if k > len(items):
#         k2 = k%len(items)
#         idx = k2
#     if len(items) == 0:
#         return []
#     while len(items) > 1:
#         if k2:
#             result.append(items.pop(idx))
#             k2 = k % len(items)
#             idx = (idx + k2) % len(items)
#         else:
#             result.append(items.pop(idx))  # kill prisoner at idx
#             idx = (idx + k) % len(items)
#
#     result.append(items[0])
#     return result

# #EX---24
# def josephus(xs, k):
#     i, ys = 0, []
#     while len(xs) > 0:
#         i = (i + k - 1) % len(xs)
#         ys.append(xs.pop(i))
#     return ys
#
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 16
# print(josephus(items, k))

# #---EX25
# def order_weight(strng):
#     array = strng.split(" ")
#     print(array)
#     array_sum = []
#     for i in array:
#         b = list(i)
#         c = [int(x) for x in b]
#         d = sum(c)
#         array_sum.append(d)
#     print(array_sum)
#     array_sum, array = zip(*sorted(zip(array_sum, array)))
#     print(array)
#     print(array_sum)
#     return " ".join(array)
#
#
# strng = "103 123 4444 99 2000 11"
# print(order_weight(strng))



# #---EX26
# def exp_sum(n):
#     return e_sum(n, 0, 1)
#
#
# def e_sum(n, current, index):
#     print("POOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCZATEK")
#     print("current:",current)
#     print("index:",index)
#     if current == n:
#         return 1
#     if current > n:
#         return 0
#
#     count = 0
#     for i in range(index, n + 1):
#         print("to jest i:", i)
#         count += e_sum(n, current + i, i)
#         print("TEEEEEEEEEERAZ COUNT:")
#         print("TO JEST COUNT: ", count)
#         print("KOOOOOOOOOOONIEC COUNT")
#     print("WYNIK:")
#     return count
#
# n = 2
# print(exp_sum(n))

# #---------------------------zadania na rozgrzewke
# def is_leap(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     return False
# year = int(input())
# print(is_leap(year))

# #---------------------------zadania na rozgrzewke
# if __name__ == '__main__':
#     n = int(input())
# result = []
# for i in range (1, n+1):
#     result.append(i)
# print(int("".join([str(x) for x in result])))

# #---------------------------zadania na rozgrzewke
# number = int(input())
# dict = set()
# for i in range(0, number):
#     country = str(input())
#     dict.add(country)
# print(len(dict))



# import pprint
# w, h = 10, 10;
# matrix = [[0 for x in range(w)] for y in range(h)]
# matrix[0][0] = 1
# matrix[0][1] = 1
# matrix[0][2] = 1
# matrix[0][3] = 1
# matrix[0][4] = 1
# matrix[0][5] = 1
# matrix[1][5] = 1
# matrix[2][5] = 1
# matrix[9][1] = 1
# matrix[9][4] = 1
# matrix[4][0] = 1
# matrix[4][9] = 1
# matrix[9][7] = 1
# matrix[9][8] = 1
# matrix[9][9] = 0
#
#
# def ship_validator(matrix):
#     ship = []
#     values = []
#     kinds = []
#     for i in range(0, 10):
#         for index, k in enumerate(matrix[i]):
#             if i == 0:
#                 if k == 1 and matrix[i+1][index] == 0 and len(ship) < 5:
#                     ship.append(k)
#                     if matrix[i][index+1] == 0 :
#                         values.append(True)
#                         kinds.append(len(ship))
#                         ship = []
#                 if k == 1 and len(ship) > 4:
#                     values.append(False)
#                     ship = []
#             if i != 0 and i != 9:
#                 if k == 1 and matrix[i+1][index] == 0 and matrix[i-1][index] == 0 and len(ship) < 5:
#                     ship.append(k)
#                     if matrix[i][index+1] == 0:
#                         values.append(True)
#                         kinds.append(len(ship))
#                         ship = []
#                 if k == 1 and len(ship) > 4:
#                     values.append(False)
#                     ship = []
#             if i == 9:
#                 if k == 1 and index != 9:
#                     if len(ship) < 4:
#                         ship.append(k)
#                         if matrix[i][index+1] == 0:
#                             values.append(True)
#                             kinds.append(len(ship))
#                             ship = []
#                     if len(ship) >= 4 and matrix[i][index+1] == 0:
#                         values.append(False)
#                         ship = []
#                 if k == 1 and index == 9:
#                     print(len(ship))
#                     if len(ship) <= 3:
#                         ship.append(k)
#                         values.append(True)
#                         kinds.append(len(ship))
#                         ship = []
#                     if len(ship) > 3:
#                         values.append(False)
#                         ship = []
#
#
#     return kinds, ship, matrix, values
#
#     return matrix
#
# pprint.pprint(ship_validator(matrix))


# def  StairCase(n):
#     for i in range(1, n+1):
#         print(" "*(n-i)+"#"*i)
# n = int(input())
# print(StairCase(n))

# def  summation(numbers):
#     return sum(numbers)
#
# numbers = [1,2,3,4,5]
# print(summation(numbers))

##ZADANIA DO HALODOKTORZE--------------------------------------------
# def  mergeStrings(a, b):
#     list_a = list(a)
#     list_b = list(b)
#     result = []
#     if len(a) < len(b):
#         for index, i in enumerate(range(0, len(b))):
#             if index <= len(a)-1:
#                 result.append(list_a[i])
#                 result.append(list_b[i])
#             else:
#                 result.append(list_b[i])
#     if len(a) > len(b):
#         for index, i in enumerate(range(0, len(a))):
#             if index <= len(b)-1:
#                 result.append(list_a[i])
#                 result.append(list_b[i])
#             else:
#                 result.append(list_a[i])
#     if len(a) == len(b):
#         for i in range(len(a)):
#             result.append(list_a[i])
#             result.append(list_b[i])
#     return "".join(result)
#
#
# a = "abc"
# b = "zsd"
# print(mergeStrings(a, b))

# def  countDuplicates(numbers):
#     result = []
#     counter = []
#     for i in range(1, 1001):
#         result.append(numbers.count(i))
#     for k in result:
#         if k > 1:
#             counter.append(k)
#     return len(counter)
#
#
# numbers = [1,1,2,2,2,3]
# print(countDuplicates(numbers))
##---------------------------------------------------------------------

# ##CODILITY-Lesson3-PermMissingElem
# def solution(A):
#     for i in sorted(A):
#         if i < 1:
#             A.remove(i)
#     A_sum = 0
#     if len(A) == 0:
#         return 1
#     if len(A) == 1:
#         if A[0] == 1:
#             return 2
#         if A[0] == 100001:
#             return 100000
#         else:
#             return 1
#     print(sorted(A))
#     for i in sorted(A):
#         A_sum += i
#     A_sum_total = sum(list(range(sorted(A)[0], sorted(A)[-1]+1)))
#     missing_element = A_sum_total - A_sum
#     print(A_sum_total, A_sum)
#     if A_sum_total == A_sum:
#         if sorted(A)[0] == 1:
#             missing_element = sorted(A)[-1]+1
#         if sorted(A)[-1] == 100001:
#             missing_element = sorted(A)[0]-1
#         if A[0] != 1 and A[-1] != 100001:
#             return 1
#     return missing_element
#
# A = [-1,0,1,2,3,4,5]
# print(solution(A))


# def my_fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     first_two = [0, 1]
#     for i in range(2, n+1):
#         first_two.append(first_two[i-1]+first_two[i-2])
#     return first_two[-1], first_two
#
# n = 50
# print(my_fibo(n))


# # CODILITY-Lesson2- OddOccurrencesInArray->O(N)
# def solution(A):
#     counter = 0
#     B = sorted(A)
#     for index, i in enumerate(B):
#         if B[index] != B[-1]:
#             if B[index] == B[index+1]:
#                 counter += 1
#             if B[index] != B[index+1]:
#                 counter +=1
#                 if counter % 2 != 0:
#                     return i
#                 if counter % 2 == 0:
#                     counter = 0
#         else:
#             return i
#
# A = [3,9,3,9,1,1,5]
# print(solution(A))
#
#
# ##-Lesson2- OddOccurrencesInArray->A.count(i) powodowalo worst-case time complexity = O(N**2)
# # def solution(A):
# #     for i in range(sorted(A)[0], sorted(A)[-1]+1):
# #         number = A.count(i)
# #         if number % 2 != 0:
# #             return i

# #CODILITY-Lesson2- CyclicRotation
# def solution(A, K):
#     if len(A) == 0:
#         return []
#     for i in range(K):
#         A.insert(0, A.pop(-1))
#     return A
#
# A = []
# K = 3
# print(solution(A,K))

# #CODILITY-Lesson4
# def solution(A):
#     A = [item for item in A if item >= 0]
#     if len(A) == 0:
#         return []
#     if len(A) == 1:
#         if A[0] < 0 or A[0] == 0 or A[0] == 2:
#             return 1
#         return A[0]+1
#     B = sorted(A)
#     result = []
#     for index, i in enumerate(B):
#         if index == len(B)-2 and B[index] == B[index+1]:
#             break
#         if index == len(B)-2 and B[index] != B[index+1]:
#             result.append(i)
#             result.append(B[index+1])
#             break
#         else:
#             if B[index] == B[index+1]:
#                 pass
#             if B[index] != B[index+1] and B[index] != B[index-1]:
#                 result.append(i)
#     print(result)
#     for i in range(0, len(result)-1):
#         print(result[i], i)
#         if result[i]+1 != result[i+1]:
#
#             return result[i]+1
#         if result[i]+1 == result[i+1]:
#             pass
#
#
#
# A =  [0, 1, 2, 3,4,6]
# print(solution(A))



# a = [1,2,3,4,5]
# for i in range(0,10):
#     try:
#         print(a[i], "index: ", i)
#     except IndexError:
#         print("nie ma tekigo indeksu w tej liście", i)
#
# d = {}
# for index, i in enumerate(range(10,21)):
#     d["index nr: {}".format(index)] = i
#
# print(d)

# #LaboratoriumEE
# import numpy, cv2
# from random import randint
# def pixel_messer(upload, save):
#     img = cv2.imread(upload)
#     for i in range(0, img.shape[1] - 1):
#         for k in range(0, img.shape[0] - 1):
#             img[k, i] = img[randint(0, img.shape[0] - 1), randint(0, img.shape[1] - 1)]
#     return cv2.imwrite(save, img)
#
# upload = '/home/tt/workspace/batman.jpg'
# save = '/home/tt/workspace/batman_messed.jpg'
#
# print(pixel_messer(upload, save))

# #EX---27-------------------------------------------------------------------------vero long exercise
# from math import sqrt
# class Vector(object):
#
#     def __init__(self, array):
#         self.array = array
#
#     def __str__(self):
#         if isinstance(self.array, str):
#             result = []
#             second_vector = []
#             for i in str(self.array):
#                 try:
#                     if i == "," or i == "]":
#                         second_vector.append(",")
#                     second_vector.append(int(i))
#                 except:
#                     ValueError
#             c = [str(i) for i in second_vector]
#             d = ''.join(c)
#             e = d.split(',')
#             for i in e:
#                 try:
#                     result.append(int(i))
#                 except:
#                     ValueError
#             return str(tuple(result))
#         return str(self.array)
#
#     def equals(self, object):
#         result = []
#         second_vector = []
#         for i in str(object):
#             try:
#                 if i == "," or i == "]":
#                     second_vector.append(",")
#                 second_vector.append(int(i))
#             except:
#                 ValueError
#         c = [str(i) for i in second_vector]
#         d = ''.join(c)
#         e = d.split(',')
#         for i in e:
#             try:
#                 result.append(int(i))
#             except:
#                 ValueError
#         return str(self), str(result)
#
#     def converter(self, new_array):
#         result = []
#         second_vector = []
#         for i in str(new_array):
#             try:
#                 if i == "," or i == "]":
#                     second_vector.append(",")
#                 second_vector.append(int(i))
#             except:
#                 ValueError
#         c = [str(i) for i in second_vector]
#         d = ''.join(c)
#         e = d.split(',')
#         for i in e:
#             try:
#                 result.append(int(i))
#             except:
#                 ValueError
#         return result
#
#     def add(self, new_array):
#         if isinstance(self.array, str) or isinstance(new_array, str):
#             result = []
#             second_vector = []
#             for i in str(new_array):
#                 try:
#                     if i == "," or i == "]":
#                         second_vector.append(",")
#                     second_vector.append(int(i))
#                 except:
#                     ValueError
#             c = [str(i) for i in second_vector]
#             d = ''.join(c)
#             e = d.split(',')
#             for i in e:
#                 try:
#                     result.append(int(i))
#                 except:
#                     ValueError
#             return str(tuple(result))
#         if len(self.array) == len(self.converter(new_array)):
#             add_result = [x+y for x, y in zip(self.array, self.converter(new_array))]
#             return Vector(add_result)
#         else:
#             raise TypeError("Different vectors lengths")
#
#     def subtract(self, new_array):
#         if isinstance(self.array, str) or isinstance(new_array, str):
#             result = []
#             second_vector = []
#             for i in str(new_array):
#                 try:
#                     if i == "," or i == "]":
#                         second_vector.append(",")
#                     second_vector.append(int(i))
#                 except:
#                     ValueError
#             c = [str(i) for i in second_vector]
#             d = ''.join(c)
#             e = d.split(',')
#             for i in e:
#                 try:
#                     result.append(int(i))
#                 except:
#                     ValueError
#             return str(tuple(result))
#         if len(self.array) == len(self.converter(new_array)):
#             add_result = [x-y for x, y in zip(self.array, self.converter(new_array))]
#             return Vector(add_result)
#         else:
#             raise TypeError("Different vectors lengths")
#
#     def dot(self, new_array):
#         if isinstance(self.array, str) or isinstance(new_array, str):
#             result = []
#             second_vector = []
#             for i in str(new_array):
#                 try:
#                     if i == "," or i == "]":
#                         second_vector.append(",")
#                     second_vector.append(int(i))
#                 except:
#                     ValueError
#             c = [str(i) for i in second_vector]
#             d = ''.join(c)
#             e = d.split(',')
#             for i in e:
#                 try:
#                     result.append(int(i))
#                 except:
#                     ValueError
#             return str(tuple(result))
#         if len(self.array) == len(self.converter(new_array)):
#             add_result = [x*y for x, y in zip(self.array, self.converter(new_array))]
#             return sum(add_result)
#         else:
#             raise TypeError("Different vectors lengths")
#
#     def norm(self):
#         if isinstance(self.array, str):
#             result = []
#             second_vector = []
#             for i in str(self.array):
#                 try:
#                     if i == "," or i == "]":
#                         second_vector.append(",")
#                     second_vector.append(int(i))
#                 except:
#                     ValueError
#             c = [str(i) for i in second_vector]
#             d = ''.join(c)
#             e = d.split(',')
#             for i in e:
#                 try:
#                     result.append(int(i))
#                 except:
#                     ValueError
#             return str(tuple(result))
#         for index, i in enumerate(self.array):
#             self.array[index] = i**2
#         return sqrt(sum(self.array))
#
#
# a = Vector('[1,2,2]')
# b = Vector([4,50,900])
#
# print(str(Vector([5, 52, 902])))
# print(a)

# ##SOME----RECURSION
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(4))
#
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(3))

#EX---28
# def string_permutations(string, n=0, result=set()):
#     if n == len(string):
#         return
#
#     for i in range(n, len(string)):
#         string_twin = [i for i in string]
#         string_twin[n], string_twin[i] = string_twin[i], string_twin[n]
#         result.add(tuple(string_twin))
#         string_permutations(string_twin, n+1)
#
#     return ["".join(x) for x in result]
#
# print(string_permutations("abcdef"))

# #EX--28 better solution
# def permutations(string):
#     result = set([string])
#     if len(string) == 2:
#         result.add(string[1] + string[0])
#
#     elif len(string) > 2:
#         for i, c in enumerate(string):
#             for s in permutations(string[:i] + string[i + 1:]):
#                 result.add(c + s)
#
#     return list(result)
#
# string = 'abc'
# print(permutations(string))
#
# #EX28---THE SHORTEST SOLUTION USING ITERTOOLS
# from itertools import permutations
# def permutations_with_itertools(string):
#     return [''.join(p) for p in permutations(string)]
#
# string = 'abc'
# print(permutations_with_itertools(string))


# #CHECKING TIME DIFFERENCES FOR LIST METHOD AND RECURSION METHOD IN FIBONACCI
# import time
#
# start_time = time.time()
#
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
# print(fibo_list(n), "list method, time: {} sek".format(time.time()-start_time))
#
# start_time2 = time.time()
#
# def fibo_recursion(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fibo_recursion(n-1)+fibo_recursion(n-2)
#
# n = 35
# print(fibo_recursion(n), "recursion method, time: {} sek".format(time.time()-start_time2))

# import datetime
# def get_start_time(schedules, duration):
#     hours = duration // 60
#     minutes = duration % 60
#     print("{}min = {}h:{}min".format(duration, hours, minutes))
#     result = []
#
#     result2 = []
#     i_id = 0
#     for i in schedules:
#         i_id += 1
#         for j in range(0, len(i)):
#             try:
#                 hours_after_check = datetime.datetime.strptime("{}".format(i[j][1]), "%H:%M").hour + hours
#                 minutes_before_check = datetime.datetime.strptime("{}".format(i[j][1]), "%H:%M").minute + minutes
#                 upper_hours = datetime.datetime.strptime("{}".format(i[j + 1][0]), "%H:%M").hour
#                 upper_minutes = datetime.datetime.strptime("{}".format(i[j + 1][0]), "%H:%M").minute
#             except:
#                 IndexError
#
#             if j == range(0, len(i))[-1]:
#                 hours_after_check = datetime.datetime.strptime("{}".format(i[-1][1]), "%H:%M").hour + hours
#                 minutes_before_check = datetime.datetime.strptime("{}".format(i[-1][1]), "%H:%M").minute + minutes
#                 upper_hours = 19
#                 upper_minutes = 0
#
#             if minutes_before_check == 60:
#                 minutes_after_check = 0
#                 hours_after_check += 1
#             if minutes_before_check > 60:
#                 hours_after_check += minutes_before_check // 60
#                 minutes_after_check = minutes_before_check % 60
#                 minutes_before_check = 0
#             if minutes_before_check < 60:
#                 minutes_after_check = minutes_before_check
#             if hours_after_check < upper_hours:
#                 predykat = True
#             if hours_after_check == upper_hours and minutes_after_check <= upper_minutes:
#                 predykat = True
#             if hours_after_check > upper_hours:
#                 predykat = False
#
#             if predykat == True:
#                 try:
#                     finally_hours = i[j][1]
#                     finally_hours_2 = i[j+1][0]
#                     result2.append(i_id)
#                     result2.append(finally_hours)
#                     result2.append(finally_hours_2)
#                     result.append(result2)
#                     result2 = []
#                 except:
#                     IndexError
#                 if j == range(0, len(i))[-1]:
#                     finally_hours = i[-1][1]
#                     finally_hours_2 = '19:00'
#                     result2.append(i_id)
#                     result2.append(finally_hours)
#                     result2.append(finally_hours_2)
#                     result.append(result2)
#                     result2 = []
#
#             # print(hours_after_check, minutes_after_check, upper_hours, upper_minutes, predykat)
#     result3 = []
#     print(result)
#     range_list = []
#     for x in range(0, len(result)-1):
#         print(range_list)
#         if result[x][0] != result[x+1][0] and result[x][0] not in range_list:
#             result3.append(result.pop(x))
#             range_list.append(result[x][0])
#         if result[x][0] == result[x+1][0] and result[x][0] not in range_list:
#             result3.append(result.pop(x))
#             range_list.append(result[x][0])
#
#
#     print(result)
#     print(result3)
#
#
#
#
# schedules = [
#   [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
#   [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
#   [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
# ]
# duration = 60
# print(get_start_time(schedules, duration))


# #MY IMPLEMENTATION OF MERGE SORT ALGORITHM
# def my_merge_sort(example):
#     if len(example) < 2:
#         return example
#
#     result = []
#     mid = int(len(example)/2)
#     y = my_merge_sort(example[:mid])
#     z = my_merge_sort(example[mid:])
#
#     while len(y) > 0 and len(z) > 0:
#         if y[0] > z[0]:
#             result.append(z.pop(0))
#         else:
#             result.append(y.pop(0))
#     result.extend(y+z)
#     return result
#
# example = [4,1,3,2]
# print(my_merge_sort(example))

#ACTUAL TEMPERATURE IN WARSAW
import requests, json
# weather = requests.get('http://api.openweathermap.org/data/2.5/forecast/city?id=756135&APPID=3bdffabc19b9f555ff88207831614ae1')
# data = weather.json()
# warsaw_temperature = data['list'][-1]['main']['temp']-273
# print(warsaw_temperature)

# #29 Reverse Polish Notation - CODEWARS
# def parse_molecule (formula):
#     result = {}
#     helper = []
#     for index, i in enumerate(formula):
#         try:
#             if i.istitle():
#                 a = i
#                 if formula[index+1].istitle():
#                     helper.append(a)
#             if not i.istitle() and ord(i) not in (40, 41):
#                 a += i
#                 if formula[index+1].istitle() or ord(formula[index+1]) in (40, ):
#                     helper.append(a)
#             if formula[index+1].isdigit():
#                 for i in range(int(formula[index+1])):
#                     helper.append(a)
#         except IndexError:
#             pass
#     for i in helper:
#
#     return helper
#
# water = 'Mg(OH2)'
# print(parse_molecule(water))

# #Codility: Lesson1 Task4
# def solution(A):
#     unique = set()
#     input = sorted(A)
#     all_elements = ((input[0]+input[-1])/2.0)*(len(input))
#     missing_element = all_elements - sum(A)
#     if len(input) == 2:
#         if input[0] == 1 and input[1] == 2:
#             return 1
#         else:
#             return 0
#     for i in input:
#         unique.add(i)
#     if input[-1] - input[0] == len(input)-1 and len(list(unique)) == len(input):
#         if input[0] != 1:
#             return 0
#         if input[0] == 1 and missing_element == 0:
#             return 1
#         else:
#             return 0
#     if missing_element == 0:
#         if len(input) == len(list(unique)):
#             return 1
#         else:
#             return 0
#     else:
#         return 0
#
# A =  [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
# print(solution(A))

# #Codility: Lesson2 Task4
# def solution(X, A):
#     assistant = list(range(1, X+1))
#     assistant_sum = sum(assistant)
#     helper = set()
#     if X not in A:
#         return -1
#     if A.count(A[0]) == len(A):
#         if A[0] == 1:
#             return 0
#         return -1
#     for y in A:
#         helper.add(y)
#     sorted_helper = sorted(list(helper))
#     if sum(sorted_helper[0:X]) == assistant_sum:
#         helper = set()
#     for index, i in enumerate(A):
#         try:
#             helper.add(i)
#             if len(list(helper)[0:X]) == len(assistant) and int((list(helper)[0]+list(helper)[X-1])/2.0*len(helper)) == assistant_sum:
#                 return index
#         except IndexError:
#             pass
#     else:
#         return -1
#
#
# A = [4,3,2,1]
# X = 4
# print(solution(X, A))

# helper = []
# apple=[[["SNo."],["Computers"],["Mobile"]],
#        [["1"],["iMac"],["iPhone"]],
#         [["2"],["Macbook"],["iPod"]]]
#
#
#
# for l in apple:
#     print(*[e[0] for e in l])
#
# print(*apple[0][0])

# pattern = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
# pattern_arabic = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
# def RomanNumerals(value):
#     if isinstance(value, str):
#         splitted = [i for i in value]
#         numbers = [pattern[i] for i in splitted]
#         result = 0
#         reversed_numbers = numbers[::-1]
#         for index, i in enumerate(reversed_numbers):
#             try:
#                 if index == 0:
#                     result += i
#                 elif index == len(numbers)-1:
#                     if reversed_numbers[index] >= reversed_numbers[index-1]:
#                         result += i
#                     else:
#                         result -= i
#                 elif reversed_numbers[index] >= reversed_numbers[index-1]:
#                     result += i
#                 elif reversed_numbers[index] < reversed_numbers[index-1]:
#                     result -= i
#             except IndexError:
#                 pass
#         return result
#     if isinstance(value, int):
#         recursion = []
#         def converter(value):
#             helper = []
#             helper2 = []
#             try:
#                 for i in pattern_arabic:
#                     if value - i >= 0:
#                         helper.append(i)
#                         helper2.append(value - i)
#                 substracted = helper[helper2.index(min(helper2))]
#                 recursion.append(substracted)
#                 converter(value-substracted)
#             except ValueError:
#                 pass
#         converter(value)
#         result = ""
#         for i in recursion:
#             if i in pattern_arabic:
#                 result += pattern_arabic[i]
#         return result
#

# romanian = "MMXVII"
# print(RomanNumerals(romanian))
# arabic = 2017
# print(RomanNumerals(arabic))

# #Codewars Roman Numerals Helper
# class RomanNumerals():
#
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def from_roman(self, test):
#         pattern = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#         splitted = [i for i in test]
#         numbers = [pattern[i] for i in splitted]
#         result = 0
#         reversed_numbers = numbers[::-1]
#         for index, i in enumerate(reversed_numbers):
#             try:
#                 if index == 0:
#                     result += i
#                 elif index == len(numbers) - 1:
#                     if reversed_numbers[index] >= reversed_numbers[index - 1]:
#                         result += i
#                     else:
#                         result -= i
#                 elif reversed_numbers[index] >= reversed_numbers[index - 1]:
#                     result += i
#                 elif reversed_numbers[index] < reversed_numbers[index - 1]:
#                     result -= i
#             except IndexError:
#                 pass
#         return result
#
#     @classmethod
#     def to_roman(self, test):
#         pattern_arabic = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",
#                           9: "IX", 5: "V", 4: "IV", 1: "I"}
#         recursion = []
#         def converter(test):
#             helper = []
#             helper2 = []
#             try:
#                 for i in pattern_arabic:
#                     if test - i >= 0:
#                         helper.append(i)
#                         helper2.append(test - i)
#                 substracted = helper[helper2.index(min(helper2))]
#                 recursion.append(substracted)
#                 converter(test - substracted)
#             except ValueError:
#                 pass
#         converter(test)
#         result = ""
#         for i in recursion:
#             if i in pattern_arabic:
#                 result += pattern_arabic[i]
#         return result
#
# print(RomanNumerals.from_roman("MMM"))
# print(RomanNumerals.to_roman(1000))

# #Codewars Longest Common Subsequence
# def lcs(x, y):
#     if len(y) > len(x):
#         result = []
#         base = [l for l in x]
#         indexes = []
#         counter = 0
#         for index, i in enumerate(x):
#             counter += 1
#             if i in y:
#                 indexes.append(index)
#                 try:
#                     if counter <= 1:
#                         if y.index(i) >= indexes[0]:
#                             result.append(base[index])
#                     if counter > 1:
#                         if y.index(i) > indexes[0]:
#                             result.append(base[index])
#                 except IndexError:
#                     pass
#         return "".join(result)
#     else:
#         result = []
#         base = [l for l in y]
#         indexes = []
#         counter = 0
#         for index, i in enumerate(y):
#             counter += 1
#             if i in x:
#                 indexes.append(index)
#                 try:
#                     if counter == 1:
#                         if x.index(i) >= indexes[0]:
#                             result.append(base[index])
#                     if counter > 1:
#                         if x.index(i) > indexes[0]:
#                             result.append(base[index])
#                 except IndexError:
#                     pass
#         return "".join(result)
# #Codewars Longest Common Subsequence - RECURSION!!!
# def lcs(x, y):
#     if len(x) == 0 or len(y) == 0:
#         return ''
#     if x[-1] == y[-1]:
#         return lcs(x[:-1], y[:-1]) + x[-1]
#     else:
#         lcs1 = lcs(x,y[:-1])
#         lcs2 = lcs(x[:-1],y)
#         if len(lcs1) > len(lcs2):
#             return lcs1
#         else:
#             return lcs2
#
# x = "abcdef"
# y = "abc"
# print(lcs(x, y))

# #Codewars Instant Runoff Voting
# import math
# def runoff(voters):
#     total_votes = len(voters)
#     first_loop = []
#     pattern = sorted(voters[0])
#     weights = []
#     for i in voters:
#         first_loop.append(i[0])
#     for i in first_loop:
#         if pattern == sorted(first_loop):
#             return None
#         if first_loop.count(i) >= math.ceil(total_votes/2):
#             return i
#     if first_loop:
#         def checker(first_loop):
#             print("im in")
#             pattern = sorted(voters[0])
#             weights = []
#             for i in pattern:
#                 weights.append(first_loop.count(i))
#             for index, i in enumerate(weights):
#                 if i == 0:
#                     weights[index] = 9999
#             for y, i in enumerate(weights):
#                 if i == min(weights):
#                     equalizer = pattern.index(first_loop[y])
#                     for k in voters:
#                         if k[0] == pattern[equalizer]:
#                             l = k[1::]
#                             first_loop[y] = l.pop(0)
#                             print(l, "to jest l")
#                 print(first_loop)
#         print(first_loop, "test")
#         return checker(first_loop)
#
#         print("end of function")
#         result = []
#         result_2 = []
#         for i in pattern:
#             result.append(first_loop.count(i))
#             result_2.append(i)
#         print(first_loop, "TEST")
#         return result_2[result.index(max(result))]


start_time = time.time()

# #Codewars Number of Proper Fractions with Denominator d
# def proper_fractions(n):
#     counter = 0
#     for i in range(1, n):
#         for k in range(2, i+1):
#             if i%k == 0 and n%k == 0:
#                 counter += 1
#                 break
#             else:
#                 pass
#     return n - (counter+1)
#
# n = 900
# print(proper_fractions(n))
# print("Classic method, TIME: {}sec".format(time.time() - start_time))
#
# start_time = time.time()
# #recursion method
# def proper_fractions(n):
#     if n == 1:
#         return 0
#     n_numbers = []
#     k = n
#     for i in range(2, n+1):
#         if n%i == 0:
#             n_numbers.append(i)
#     return checker(n, 0, k, n_numbers)
#
# def checker(n, counter, k, n_numbers):
#     if n > 0:
#         for i in n_numbers:
#             if n % i == 0:
#                 counter += 1
#                 break
#         return checker(n - 1, counter, k, n_numbers)
#     if n == 0:
#         return k - counter
#
# n = 1000
# print(proper_fractions(n))
# print("Recursion method, TIME: {}sec".format(time.time() - start_time))

# #recursion method
# def proper_fractions(n):
#     if n == 1:
#         return 0
#     n_numbers_ = []
#     k = n
#     for i in range(2, n+1):
#         if n%i == 0:
#             n_numbers_.append(i)
#     sieve = [True] * n
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if sieve[i]:
#             sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
#     primes = [2]
#     for i in range(3,n,2):
#         if sieve[i]:
#             primes.append(i)
#     n_numbers = []
#     for i in n_numbers_:
#         if i in primes:
#             n_numbers.append(i)
#     return checker(n, 0, k, n_numbers)
#
# def checker(n, counter, k, n_numbers):
#     if n > 0:
#         for i in n_numbers:
#             if n % i == 0:
#                 counter += 1
#                 break
#         return checker(n - 1, counter, k, n_numbers)
#     if n == 0:
#         return k - counter
#
# n = 900
# print(proper_fractions(n))
# print("Recursion method, TIME: {}sec".format(time.time() - start_time))
#
#
# def proper_fractions(n):
#     counter = 0
#     for i in range(1, n):
#         for k in range(2, i+1):
#             if i%k == 0 and n%k == 0:
#                 counter += 1
#                 break
#             else:
#                 pass
#     return n - (counter+1)
#
# def proper_fractions_2(n):
#     helper = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             helper.append(I)
#
# print(proper_fractions_2(15))

# def palindrome2(n, c):
#     if n%2 != 0:
#         result = [c[-1]]
#     else:
#         result = [c[-1], c[-1]]
#     counter = 0
#     while len(result) <= n-1:
#         result.append(c[counter])
#         result.insert(0, c[counter])
#         counter += 1
#     return "".join(result)
#
# def p(n, c):
#     return c+c[-1]*(n-2*len(c)+1)+c[-2::-1]
# #CODEWARS: One Line Task: Palindrome String -> best solution!
# palindrome=lambda n,c: c[:0:-1]+c[0]*(n-2*len(c)+1)+c
#
#
# n = 6
# c = "abc"
#
# print(palindrome)

#CODEWARS: Soundex
def soundex(name):
    first_split = name.split(" ")
    result = []
    for index, i in enumerate(first_split):
        helper = [first_split[index][0]]
        n = [i for i in first_split[index][1::] if i.upper() != "H" and i.upper() != "W"]
        for x, j in enumerate(n):
            if x == 0 and j == helper[0]:
                break
            if j.upper() in ["B", "F", "P", "V"]:
                helper.append("1")
            if j.upper() in ["C", "G", "J", "K", "Q", "S", "X", "X"]:
                helper.append("2")
            if j.upper() in ["D", "T"]:
                helper.append("3")
            if j.upper() == "L":
                helper.append("4")
            if j.upper() in ["M", "N"]:
                helper.append("5")
            if j.upper() == "R":
                helper.append("6")
        print(helper)
        result.append(helper)

    for i in result:
        for j in i:
            if i.count(j) > 1:
                i.remove(j)
        if len(i) < 4:
            times = 4 - len(i)
            for j in range(times):
                i.append("0")
    for i in result:
        if len(i) > 4:
            result.append(i[0:4])
            result.remove(i)
    return " ".join(["".join(i) for i in result])

name = 'Cccc'
print(soundex(name))
























