Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(1,2,3,'sam')
>>> type(t)
<class 'tuple'>
>>> l=list(t)
>>> print(l)
[1, 2, 3, 'sam']
>>> list=[1,2,3,4,5]
>>> list.append(9)
>>> print(list)
[1, 2, 3, 4, 5, 9]
>>> list.remove(3)
>>> print(list)
[1, 2, 4, 5, 9]
>>> print(max(list))
9
>>> print(min(list))
1
>>> tuple=('s','a','m',1,2,3)
>>> tuple=tuple[::-1]
>>> print(tuple)
(3, 2, 1, 'm', 'a', 's')
>>> 