Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #day 7 task
>>> 
>>> # python module example
>>> def add(a, b):


   result = a + b
   return result

>>> #2
>>> #pip3 install pandas
>>> #installing pandas
Collecting pandas
  Downloading pandas-1.1.4-cp39-cp39-win_amd64.whl (8.9 MB)
     |████████████████████████████████| 8.9 MB 6.8 MB/s
Collecting pytz>=2017.2
  Downloading pytz-2020.4-py2.py3-none-any.whl (509 kB)
     |████████████████████████████████| 509 kB 3.3 MB/s
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 3.3 MB/s
Collecting numpy>=1.15.4
  Downloading numpy-1.19.4-cp39-cp39-win_amd64.whl (13.0 MB)
     |████████████████████████████████| 13.0 MB 3.3 MB/s
Collecting six>=1.5
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: pytz, six, python-dateutil, numpy, pandas
  WARNING: The script f2py.exe is installed in 'C:\Users\ELCOT\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-1.19.4 pandas-1.1.4 python-dateutil-2.8.1 pytz-2020.4 six-1.15.0
WARNING: You are using pip version 20.2.3; however, version 20.2.4 is available.
You should consider upgrading via the 'C:\Users\ELCOT\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip' command.

SyntaxError: invalid syntax
>>> 
>>> #3
>>> 
>>> import random
>>> print("random integer is ",random.randint(0,9))
random integer is  4
>>> 
>>> 
>>> #4
>>> 
>>> import sys
>>> for p in sys.path:
	print(p)

	

C:\Windows\system32
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.240.0_x64__qbz5n2kfra8p0
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.240.0_x64__qbz5n2kfra8p0\python39.zip
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.240.0_x64__qbz5n2kfra8p0\DLLs
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.240.0_x64__qbz5n2kfra8p0\lib
C:\Users\ELCOT\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0
C:\Users\ELCOT\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.240.0_x64__qbz5n2kfra8p0
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.240.0_x64__qbz5n2kfra8p0\lib\site-packages
>>> 
>>> 
>>> #5
>>> 
>>> #pip3 uninstall pandas
Found existing installation: pandas 1.1.4
Uninstalling pandas-1.1.4:
  Would remove:
    c:\users\elcot\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages\pandas-1.1.4.dist-info\*
    c:\users\elcot\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages\pandas\*
Proceed (y/n)? y
  Successfully uninstalled pandas-1.1.4
  
SyntaxError: invalid syntax
>>> 