import math

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

#---EX13 --> convert sum of two digits into binary - MY SOLUTION - I DIDNT FINISH IT
# def add_binary(a,b):
#     binary = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8]
#     sum_a_b = a + b
#     result = []
#     print(sum_a_b-1)
#     if sum_a_b % 2 == 0:
#         for index, x in enumerate(binary):
#             if x == sum_a_b:
#                 print(index, x)
#                 for i in range(0, index):
#                     result.append(0)
#                 result.append(1)
#                 result.reverse()
#                 return ''.join(str(k) for k in result)
#             else: 
#                 sort = sorted(binary)
#                 binary.append(sum_a_b)
#                 for i, k in enumerate(sort):
#                     if k == sum_a_b:
#                         print(sort[i]-sort[i-1])
#                         if sort[i]-sort[i-1]
#                         return(i, k, sort)

# #---EX13 --> simplest solution      
# def add_binary(a,b):
#     sum_a_b = a + b
#     return "{0:b}".format(sum_a_b)  
#     
# 
# a = 2
# b = 32
# print(add_binary(a,b))

#---EX14 - sum of left side of index equal sum of right side of index and return index
def find_even_index(arr):
    a = 0
    b = 0
    result = []
    reverse_result = []
    final = []
    reversed = arr[::-1]    
    for x in arr:               
        a += x
        result.append(a)      
    for y in reversed:
        b += y
        reverse_result.append(b)
    for (x1, x2) in zip(result, reverse_result[::-1]):
        c = x1 - x2
        final.append(c)  
    for index, z in enumerate(final):
        if 0 not in final:
            return -1
        else:
            if z == 0:
                return index

arr = [100, 1, 1, 9, 20, 20, 50]

print(find_even_index(arr))
    
    
    
    
    
    
    
    
    
    
    
        
   

    


    