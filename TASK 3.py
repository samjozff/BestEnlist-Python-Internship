Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={"soap":10,"shampoo":5,"oil":20}
>>> dict2={"tamilnadu":"chennai","karnataka":"banglore"}
>>> dictionary=dict1.copy()
>>> dictionary.update(dict2)
>>> print(dictionary)
{'soap': 10, 'shampoo': 5, 'oil': 20, 'tamilnadu': 'chennai', 'karnataka': 'banglore'}
>>> print(dict1.pop("shampoo"))
5
>>> print(dict2)
{'tamilnadu': 'chennai', 'karnataka': 'banglore'}
>>> print(dict1)
{'soap': 10, 'oil': 20}
>>> capitals=['tamilnadu','karnataka']
>>> states=['chennai','banglore']
>>> result=dict(zip(capitals,states))
>>> print(result)
{'tamilnadu': 'chennai', 'karnataka': 'banglore'}
>>> set1={1,2,3,4,5,6,8,11,8}
>>> print(len(set1))
8
>>> set2={3,5,1,4,5,6,7,5,3,2,7}
>>> set3={4,2,5,7,8,5,8,9,6,2,4}
>>> print(set2-set3)
{1, 3}
>>> 