'''
Python has the following data types built-in by default,in these categories:

Text Type: str

Numeric Types: int,float,complex

Sequence Types: list,tuple,range

Mapping Type: dict

Set Types: set,frozenset

boolean Type: bool

Binary Types: bytes, bytearray, memoryview

None type: Nonetype


'''

x = "Hello World"#str
x = 20 #int
x = 20.5 #float
x = 1j+1 # complex


x = ["apple","bananna","cherry"]#list
x = ("apple","bannana","cherry")#tuple
x = range(6)#range


x = {"name":"Saksham","age":"36"}#dict


x = frozenset({"apple","bannana","cherry"})

x = True #boolean

x = b"hello" #creates an array kinda thing in which ASCII value of letters are stored

# print(x[0]) will print 104 as ASCII value of h is 104

x = bytearray(5)

x = memoryview(bytes(5))

x = None
