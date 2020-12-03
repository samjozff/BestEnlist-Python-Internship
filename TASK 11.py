Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Best Enlist Python Program
>>> 
>>> #Exercise
>>> 
>>> #Day 11
>>> 
>>> #1.Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
>>> def merge(a,b):
	merge = [(a[i],b[i]) for i in range(0, len(a))]
	return merge

>>> a = [1,2,3]
>>> b = ['a','b','c']
>>> print(merge(a,b))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> 
>>> #2.First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
>>> a = []
>>> for i in range (1,9):
	a.append(i)

>>> b = ['a','b','c','d','e','f','g','h']
>>> c = list(zip(a,b))
>>> c
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h')]
>>> 
>>> #3.Using sorted() function, sort the list in ascending order.
>>> l=[3,6,5,3,2,8,7,9,0,1]
>>> l.sort()
>>> l
[0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
>>> 
>>> #4.Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
>>> n = [1,2,4,5,3,7,8,12,56,43,44,20,13]
>>> def even(num):
	if(num % 2) == 0:
		return False
	else:
		return True


	
>>> odd = filter(even,n)
>>> print(list(odd))
[1, 5, 3, 7, 43, 13]
>>> 