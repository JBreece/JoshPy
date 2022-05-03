# Iteration and Iterables


words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print(words)
print([len(word) for word in words])
# list comprehension syntax:
# [expr(item) for item in iterable]
# set comprehension syntax is the same but with curly braces:
# {expr(item) for item in iterable}
print({len(word) for word in words})
# notice that because it's a set and not a list, it's unordered.

# dictionary comprehension syntax:
# also in curly braces but needs a key and value separated by a colon:
# {
# key_expr(item): value_expr(item)
# for item in iterable
# }
country_to_capital = {"United Kingdom": "London",
                      "Brazil": "Brasilia",
                      "Morocco": "Rabat",
                      "Sweden": "Stockholm"}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
# in this example the "capital: country" is "key_expr(item): value_expr(item)"
# and for item in iterable is "for country, capital (multiple items, comma delimited) in country_to_capital.items()"
from pprint import pprint as pp
pp(capital_to_country)
# note here, you have to use <dict>.items() to get the actual keys and values from the dictionary - otherwise this can happen:
words = ["hi", "hello", "foxtrot", "hotel"]
print({x[0]: x for x in words})
# notice only 1 "h" word is kept because it overwrites it if you don't use <dict>.items() (because iterating over a dictionary without doing this yields only the keys, not the keys and values, so it sees duplicate keys and keeps overwriting until it gets to the last one)

# filtering comprehensions
from math import sqrt
def is_prime(x):
    """Primality-testing predicate function"""
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
print([x for x in range(101) if is_prime(x)])

# iteration protocols
# "iterable" means it can use iter(), "iterator" means it can use next()
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # if you reach the end of an iterable and you try to call next() then an exception is thrown
def first(iterable):
    """When passed an iterable object, returns the first item in that series, or when empty passes a value error"""
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(["1st", "2nd", "3rd"]))
print(first({"1st", "2nd", "3rd"}))
# print(first(set())) # this passes an empty set, so it throws a value error

# generator functions
def gen123():
    """defines a generator function, which is an iterable object"""
    yield 1
    yield 2
    yield 3
g = gen123()
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # if you reach the end of an iterable and you try to call next() then an exception is thrown
h = gen123()
i = gen123()
print(h, i) # notice these are 2 distinct objects.  This is because each call to a generator function creates a new object.
print(next(h))
print(next(h))
print(next(i)) # because they are unique, they iterate separately
# also a note here, "yield" is what stops a generator function.  so any code between the yields is run until it hits the next "yield" in the function.