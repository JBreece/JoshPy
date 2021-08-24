# test loop
for i in range(5):
    x = i * 10
    print(x)


# importing something
import math
n = 5
k = 3
print(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
from math import factorial
print(factorial(n) / (factorial(k) * factorial(n - k)))
# on the REPL you can use help(math)


# different ways to use ints:
a = 10
print("10 = " + str(a))
a = 0b10 # binary
print("0o10 = " + str(a))
a = 0o10 # octal
print("0b10 = " + str(a))
a = 0x10 # hexadecimal
print("0x10 = " + str(a))
a = 3e8 # scientific notation
print("3e8 = " + str(a))
a = None
print("None = " + str(a))


#quick note on bool, any variable which is empty is evaluated as "False", like an empty string would be false


#control flow
if True:
    print("It's true!")
else:
    print("It's false!")

a = "test string"
if (a == "test string"):
    print("test string")
elif(a):
    print(a)
else:
    print("empty string")

a = "non empty string"
if (a == "test string"):
    print("test string")
elif(a):
    print(a)
else:
    print("empty string")

a = ""
if (a == "test string"):
    print("test string")
elif(a):
    print(a)
else:
    print("empty string")

c = 5
while c != 0:
    print(c)
    c -= 1

# while True:
#     pass
# ctrl + c to get out of this endless loop
# also commenting this out for now so i don't have to do this every time

# while True:
#     response = input()
#     if int(response) % 7 == 0:
#         break
# user must input a value divisible by 7 to exit (input mod 7)
# also commenting this out for now so i don't have to do this every time


#strings, collections (arrays/lists), and iteration
print("This is\na multiline\nstring")
print("This is\n\ta tab line")
print("This is a \" in a string")
path = r"C:\Users\Josh\Documents\python" # r = raw string
print(path)
s = 'parrot'
print(s[4])
print(type(s[4])) # there is no "char" in python, only strings
c = "oslo"
print(c.capitalize())
print(b"data")
d = b"some bytes"
print(d[0])
print(d.split())
norsk = "Jeg begynte å fortære en sandwich mens jeg kjørte taxi på vei til quiz"
data = norsk.encode("utf8")
print(data)
norwegian = data.decode("utf8")
print(norwegian == norsk)
print(norwegian)

# "strings" are immutable in python:
name_1 = "test"
print(id(name_1), name_1)
name_1 = "test2"
print(id(name_1), name_1) # notice when you set a new value for name_1 it actually creates a new object
name_2 = "test"
print(id(name_2), name_2) # notice the ID for name_2 is the same as name_1
# also note that "lists" in python are mutable, unlike strings.
# also lists can be heterogenous:
a = ["apple", 7, "pear"]
a.append(3.14)
print(a)
b = list("test") # list constructor
print(b)

# "dict" or dictionaries are a fundamental data structure in python
# maps keys to values, also known as maps or associative arrays
d = {"alice": "839-913-2057", "bob": "523-132-6923", "eve": "581-134-2740"}
print(d["alice"])

# iteration (for loops)
cities = ["London", "New York", "Paris"]
for city in cities:
    print(city)
colors = {"crimson": 0xdc143c, "coral": 0xff7f50, "teal": 0x008080}
for color in colors:
    print(color, colors[color])


# Modularity
