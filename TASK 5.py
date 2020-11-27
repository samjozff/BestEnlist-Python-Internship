Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #EXERCISE
>>> #1
>>> 
>>> a=int(input("enter the first number :"))
enter the first number :20
>>> b=int(input("enter the second number :"))
enter the second number :10
>>> #addition
>>> print("addition of the two numbers is ",a+b)
addition of the two numbers is  30
>>> #subtraction
>>> print("subtraction of the two number is ",a-b)
subtraction of the two number is  10
>>> #multiplication
>>> print("multiplication of the two number is ",a*b)
multiplication of the two number is  200
>>> #division
>>> print("division of the two numbers is ",a/b)
division of the two numbers is  2.0
>>> 
>>> #2
>>> 
>>> name=input("Enter Name :")
Enter Name :SAM
>>> temp=int(input("Enter Body Temperature :"))
Enter Body Temperature :98
>>> def covid(Patient_name,temp=98):
	print("Patient name is ",patient_name)
	print("Body temperature is",temp)

	
>>> covid(name,temp)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    covid(name,temp)
  File "<pyshell#22>", line 2, in covid
    print("Patient name is ",patient_name)
NameError: name 'patient_name' is not defined
>>> def covid(patient_name,temp=98):
	print("Patient name is ",patient_name)
	print("Body temperature is",temp)

	
>>> covid(name,temp)
Patient name is  SAM
Body temperature is 98
>>> 