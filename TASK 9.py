Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Best Enlist Python Internship
>>> 
>>> #DAY 9
>>> 
>>> #Exercise :
>>> 
>>> #1.Create a lambda function that multiplies argument x with argument y.
>>> s = lambda x,y : x * y
>>> print(s(3 , 9))
27
>>> 
>>> #2.Write a Python program to create Fibonacci series to n using Lambda.
>>> def fibonacci(count):
	list1 = [0,1]
	any(map(lambda _:list1.append(sum(list1[-2:])),range(2,count)))
	return list1[:count]

>>> print(fibonacci(10))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> 
>>> #3.Write a Python program that multiply each number of given list with a given number.
>>> list1 = [1,2,4,5,6,7]
>>> numb = 3
>>> print("list1 :",list1)
list1 : [1, 2, 4, 5, 6, 7]
>>> print("number :",numb)
number : 3
>>> multiplying_with_list = list(map(lambda list1 : list1 * numb,list1))
>>> print('\nmultiplied numbers :',' '.join(map(str,multiplying_with_list)))

multiplied numbers : 3 6 12 15 18 21
>>> 
>>> #4.Write a Python program to find numbers divisible by 9 from a list of numbers
>>> 
>>> list1 = [8,9,18,27,30,36,54,65,73,81]
>>> result = list(filter(lambda a:(a%9 ==0), list1))
>>> print("divisible by 9 are ",result)
divisible by 9 are  [9, 18, 27, 36, 54, 81]
>>> 
>>> #5.Write a Python program to count the even numbers in a given list of integers.
>>> list1 = [1,2,3,5,6,7,8,9,22,44,33,35,65,68]
>>> print("list1 :",list1)
list1 : [1, 2, 3, 5, 6, 7, 8, 9, 22, 44, 33, 35, 65, 68]
>>> find_even = len(list(filter(lambda x:(x % 2 == 0), list1)))
>>> print("number of even numbers in a list1 : ",find_even)
number of even numbers in a list1 :  6
>>> 