Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #DAY 6 TASK :
>>> 
>>> #1
>>> 
>>> list1=[1,3,4,6,8,9,10]
>>> list2=[]
>>> for i in range(0,len(list1)):
	list2.append(list1[i]+2)

	
>>> print("final list : ",str(list2))
final list :  [3, 5, 6, 8, 10, 11, 12]
>>> 
>>> #2
>>> 
>>> for i in range(5,0,-1):
	for j in range(i,0,-1):
		print(j,end="")
	print()

	
54321
4321
321
21
1
>>> 
>>> #3
>>> 
>>> a= -1
>>> b= 1
>>> c= a+b
>>> print(c)
0
>>> for i in range(1,10,1):
	c= a+b
	print(c)
	a=b
	b=c

	
0
1
1
2
3
5
8
13
21
>>> #4
>>> 
>>> num = int(input("enter a number : "))
enter a number : 371
>>> sum = 0
>>> temp = num
>>> while temp >0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10

	
>>> if num == sum:
	print(num,"is an armstrong number ")
else :
	print(num,"is not a armstrong no.")

	
371 is an armstrong number 
>>> 
>>> #5
>>> 
>>> for i in range(1,10,1):
	k = 9
	j = 9*i
	print("9 x i =",j)

	
9 x i = 9
9 x i = 18
9 x i = 27
9 x i = 36
9 x i = 45
9 x i = 54
9 x i = 63
9 x i = 72
9 x i = 81
>>> 
>>> #6
>>> 
>>> num = float(input("enter a number : "))
enter a number : -3
>>> if num > 0:
	print("positive number")
elif num ==0:
	print("zero")
else:
	print("negative number")

	
negative number
>>> 
>>> #7
>>> 
>>> import math
>>> x = 0.75
>>> print(math.sin(x))
0.6816387600233341
>>> 
>>> #8 days to age
>>> 
>>> 
KeyboardInterrupt
>>> days = 2020
>>> age = int(days/365)
>>> print("ages :",age)
ages : 5
>>> 
>>> #9
>>> 
>>>  print("calculator")
 
SyntaxError: unexpected indent
>>> print("calculator")
calculator
>>> print("2.subtract")
2.subtract
>>> print("3,multiply")
3,multiply
>>> print("3.multiply")
3.multiply
>>> print("4.divide")
4.divide
>>> 
KeyboardInterrupt
>>> ch=int(input("enter the choice(1-4) : "))
enter the choice(1-4) : 3
>>> if ch==1:
	a=int(input("a :"))
	b=int(input("b :"))
	c = a+b
	print("c :",c)
elif ch==2:
	a=int(input("a :"))
	b=int(input("b :"))
	c = a-b
	print("c :",c)
elif ch==3:
	a=int(input("a :"))
	b=int(input("b :"))
	c = a*b
	print("c :",c)
elif ch==4:
	a=int(input("a :"))
	b=int(input("b :"))
	c = a/b
	print("c :",c)
else:
	print("invalid choice")

	
a :20
b :5
c : 100
>>> 