Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Best Enlist Python Internship
>>> 
>>> #Exercise
>>> 
>>> #1.Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
>>> import re
>>> 
>>> def characters(string):
	char = re.compile(r'[^a-zA-Z0-9]')
	string = char.search(string)
	return not bool(string)

>>> print(characters(input()))
s@m
False
>>> #2.Write a Python program that matches a word containing 'ab'.
>>> import re
>>> def text_match(text):
        patterns = '\t*ab.\t*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

        
>>> print(text_match("abraham"))
Found a match!
>>> 
>>> #3.Write a Python program to check for a number at the end of a word/sentence.
>>> import re
>>> word = re.compile(r'[0-9]$')
>>> print(bool(regenerate.search(input())))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(bool(regenerate.search(input())))
NameError: name 'regenerate' is not defined
>>> print(bool(word.search(input())))
sam2020
True
>>> #4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
>>> import re
>>> results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
>>> print("Number of length 1 to 3")
Number of length 1 to 3
>>> for n in results:
	print(n.group(0))

	
1
12
13
345
>>> #5.Write a Python program to match a string that contains only uppercase letters
>>> import re
>>> def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

>>> print(text_match("The quick brown fox jumps over the lazy dog."))
Not matched!
>>> print(text_match("Python_Exercises_1"))
Found a match!
>>> 