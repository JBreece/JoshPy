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
# function
def square(x):
    return x * x
print("5 squared is ", square(5))

# just a note on terminology, "dunder" method means a special function like __init__
# dunder just means "Double UNDERscore"

# __name__ or "dunder name" allows us to detect whether a module is run as a script or imported into another module
# as in, if you run it from the REPL then it'll say "__name__" but if you run it as a script from cmd (without using python)
# then you'll see "__main__" instead
# for example in our "words.py" script if you add a line that says "print(__name__)" you'll see a different value for each scenario ^

#also note in the "words.py" that if __name__ == '__main__': allows our module to be executable and importable
#also note the """ <info> """ comments allow you to call help() on a given function, or for the module as a whole.  see words.py

a = 123
print("a is ", id(a))
a = 456
print("a is now ", id(a))
# ints are immutable, so a new object in memory is created rather than reassigning the existing object to a new value.
b = 789
print("is a = b?", id(a) == id(b))
b = a
print("is a = b?", a is b) # "is" operator is the same as "id(a) == id(b)"
r = [2, 4, 6]
print("r is ", id(r))
s = r
s[1] = 17
print("r is still ", id(r), "because arrays are mutable in python") # no new object is created.
print(s is r)


# VERY IMPORTANT TO KNOW - ALL ARGUMENTS PASSED IN FUNCTIONS IN PYTHON ARE PASSED BY REFERENCE
# this means if you change the parameter within that function, it will ACTUALLY change it (so annoying why cant every language just be C)
a = [1, 2, 3]
def modify(b):
    b.append(4)
    print("b =", b)
modify(a)
print(a) # notice here that a has ACTUALLY been changed, not just passed by value for the sake of the function

a = [1, 2, 3]
def modify(b):
    b = [4, 5, 6]
    print("b =", b)
modify(a)
print(a) # in this case because we assigned b to a new value rather than modifying it, then that reassignment created a new object.  so a was unchanged in this case.

a = [1, 2, 3]
def modify(b):
    c = b.copy()
    c.append(4)
    print("c =", c)
modify(a)
print(a) # copy

# just another related note, if you have a default argument passed in your function, make sure to have only immutable values passed in that default arg.  otherwise, because default will change based on what you do in the function:
def add_spam(menu=[]):
    menu.append("spam")
    return menu
breakfast = ['bacon', 'eggs']
print(add_spam(breakfast)) # seems like it's working fine
print(add_spam()) # still seems ok
print(add_spam()) # uh oh why is there already a spam there
print(add_spam()) # oh dear god i'll never use a mutable value as a default value again

def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu
print(add_spam())
print(add_spam())
print(add_spam()) # this is fine now

# how to go up in scope within a function (is this recommended?  seems like bad practice):
count = 0
def show_count():
    print(count)
def set_count(c):
    count = c
show_count()
set_count(5)
show_count() # see here that "count" has not changed - this is because "count" within set_count is local to that function.  to change the global "count" variable you need to do the following:
def set_count(c):
    global count
    count = c
show_count()
set_count(5)
show_count() # now it changes.  (again, not sure if it's best practice to edit global variables from within a local scope.  maybe it's ok in python?)