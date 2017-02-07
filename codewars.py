import math
from subprocess import list2cmdline

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
# n = 10    
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

##TASK1
# import itertools
# def solution(N):
#     list_N = [int(x) for x in str(N)]
#     combinations = set(itertools.permutations(list_N))      
#     list_comb = list(combinations)
#     print(len(list_comb))
#     if len(list_comb) >= 100000000:
#         return -1 
#     result = []
#     for i in list_comb:
#         r = ''.join(map(str, i))
#         result.append(int(r))
#     return max(result)   
# 
# 
# N = 123456789123
# print(solution(N))

##TASK3
# def solution(N):
#     numbers = [0, 1]
#     for i in range(2,N-1):
#         numbers.append(numbers[i-1]+numbers[i-2])
#     fibonacci = sum(numbers)+1    
#     return fibonacci%1000000    
# 
# N = 36
# print(solution(N))

##TASK5
# def solution(A):
#     del A[0]
#     del A[-1]
#     print(A)
#     result = []
#     result.append(A[0]+A[-2])
#     result.append(A[0]+A[-1])
#     result.append(A[1]+A[-1]) 
#     print(result)   
#     return min(result)     
# 
# A = [13, 5, 12, 6, 3, 7, 2, 4, 6, 3, 7, 2, 4, 6, 3, 7, 2, 4, 6, 3, 7, 2, 4, 6, 3, 7, 2, 113, 41, 33, 41]
# print(solution(A))
##TASK2
# import itertools
# def solution(A): 
#     combs_list = []    
#     result = [] 
#     longest = []
#     for i in range(1,len(A)+1):
#         element = [list(x) for x in itertools.combinations(A,i)]
#         combs_list.append(element)
#     for i in combs_list:
#         for j in i:
#             if len(j) <= 1:
#                 difference_j = 0
#                 result.append(j)
#             else:
#                 difference_j = max(j)-min(j)
#                 if difference_j <= 1:
#                     result.append(j)
#                 else:
#                     pass
#     for i in result:
#         longest.append(len(i))
#     return max(longest)
#     
# 
# A = [6, 10, 6, 9, 7, 8]
# 
#         
# print(solution(A))  

#TASK4
def solution(A, B):
    result_A = []
    result_B = []
    for index, i in enumerate(A):
        value = i*(-2)**index
        result_A.append(value)
    for index, k in enumerate(B):
        value = k*(-2)**index
        result_B.append(value)
    value = sum(result_A) + sum(result_B)   
    return value # need to return it in this binary version
    
    
#     sum_a_b = A+B
#     return "{0:b}".format(A)
A = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
B = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]
print(solution(A, B)) 

    


    