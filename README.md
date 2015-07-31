# compy
A dialect of python for competition coding

Allows infix-style function calling, making python's native functional tools much more useful.

Example:

range(10):  
|> map(lambda x: x*x, $)  
|> print str($)

which is the same as the standard python:

tmp = range(10)  
tmp2 = map(lambda x: x*x, tmp)  
print str(tmp2)
