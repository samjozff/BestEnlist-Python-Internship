#Best Enlist Python Internship

#DAY 12
 
#Exercise

#1.Create a JSON of all object types and import the JSON into a SQL Database
 
#dict

import json
x = {"name": "sam","age": 30,"city":"chennai"}
y = json.dumps(x)
print(y)
{"name": "sam", "age": 30, "city": "chennai"}
 
#list
 
import json
x = ["joseph","sam","chennai"]
y = json.dumps(x)
print(y)
["joseph", "sam", "chennai"]

#tuple

x = (3)
y = json.dumps(x)
print(tuple(y))
('3',)

string

import json
x = {"name": "sam","age": 20,"city":"chennai"}
string = json.dumps(x)
print(string)
{"name": "sam", "age": 20, "city": "chennai"}

#int
#float
 
import json
a = 3
b = 2.2
y = json.dumps(int(a+b))
print(y)
5
y = json.dumps(float(a+b))
print(y)
5.2
