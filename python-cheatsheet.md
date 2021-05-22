# Python 3 Cheatsheet
#### References:

These notes came from the following sources:

    INTRODUCING PYTHON (1st Edition)
    Bill Lubanovic
    O'Reilly 2015

    Quick reference:
    * Ch. 7 on string manip/regex, binary data handling
    * Ch. 8 on file I/O
    * Ch. 10 on system functions, including time functions
    * Ch. 12 on debugging with pdb 
    * Appendix C on SciPy and NumPy
    * Appendix D on installing Python

Index:
[Strings](#strings)

[Lists](#lists)
[Tuples](#tuples)
[Dictionaries](#dictionaries)
[Sets](#sets)
[Combining Data Structures](#combining-data-structures)
[If/While Statements](#if-while)
[For Loops](#for)
[Zip](#zip)
[Ranges](#ranges)
[List Comprehensions](#list-comprehensions)
[Dictionary Comprehensions](#dictionary-comprehensions)
[Set Comprehensions](#set-comprehensions)
[Generator Comprehensions](#generator-comprehensions)
[Functions](#functions)
[Generator Function](#generator-function)
[Decorator Function](#decorator-function)
[Namespaces](#namespaces)
[Exception Handling](#exception-handling)
[Creating Modules](#creating-modules)
[Packages](#Packages)
[Objects](#objects)
[Code Checking with Pylint](#code-checking-with-pylint)
[Unit Testing](#testing-with-unittest)
[Error Logging](#logging-error-messages-with-logging)
[Miscellaneous](#miscellaneous)

---

### Strings

The `print()` function adds spaces between strings, and a newline at the end
```python
print(99,'bottles','would be enough.\n')   # 99 bottles would be enough
```

Strings can be enclosed by either single or double quotes
```python
a = 'snap'; print(a)            # snap
b = "crackle"; print(b,'\n')    # crackle
```

You can combine quotes so that strings can contain ' or "
```python
c = "and I said 'nay' to him"; print(c)     # and I said 'nay' to him 
d = 'a captive double quote (")'; print(d)  # a captive double quote (") 
```

You can also just use escape characters
```python
esc = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(esc)
# "I did nothing!" he said. "Not that either! Or the other thing."
```

Triple quotes are useful for multiline strings without having to use \n (note that if you had used single quotes here, you would get an EOL error)
```python
multi = '''
Here is a multiline string
containing a double quote (")
'''; print(multi)
#  Here is a multiline string
#  containing a double quote (")
```

Empty strings can be created in a number of ways
```python
e = ''; 
f = ""; 
g = ''''''; 
h = """"""; 
```

Note that Python does not add spaces when concatenating strings, but the `print()` function does!
```python
duck  = 'Duck.'
goose = 'Goose.'
print(duck + duck + goose)
print(duck,duck,goose)
# Duck.Duck.Goose.
# Duck. Duck. Goose.
```

Blank strings are useful as a starting point for concatenation
```python
bottles = 99
base    = ''
base   += 'current inventory: '
base   += str(bottles)
print(base, '\n')
# current inventory: 99
```

You can duplicate strings with *
```python
start = 'Na' * 8
end   = 'Batman!'
print(start,end,'\n')
# NaNaNaNaNaNaNaNa Batman!
```

You can extract a character from a string by specifying its offset, or slicing. The syntax is `[start:end:step]`
```python
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])      #a
print(letters[-1])     #z
print(letters[11:15])  #lmno
print(letters[22:])    #wxyz
print(letters[-4:])    #wxyz
print(letters[22:-1])  #wxy
print(letters[22:-10]) #empty string!
print(letters[::7])    #ahov; start to end in steps of 7
print(letters[::-1])   #zyxwvutsrqponmlkjihgfedcba; backwards
```

More explicitly: reverse all characters in a string
```python
word = 'abcde'
word[::-1]
'edcba'
```

You can split strings quite easily
```python
todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(',')) # split by commas
# ['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']

print(todos.split())    # default is to split by spaces
# ['get', 'gloves,get', 'mask,give', 'cat', 'vitamins,call', 'ambulance']
```

Note the split behaviour for repeating separator strings
```python
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
#  ['a', 'b', '', 'c', 'd', '', '', 'e']

print(splitme.split('//'))
# ['a/b', 'c/d', '/e']
```

How to join lists into a single string
```python
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('\nFound and signing book deals:', crypto_string)
# Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster
```

How to create a paragraph out of a list
```python
para = ['line 1', 'line 2', 'line 3']
para_string = '\n'.join(para)
print(para_string)
# line 1
# line 2
# line 3
```

Illustrating some general string functions
```python
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt'''
print(len(poem))              #249
print(poem.startswith('All')) #True
print(poem.endswith('Fin'))   #False
word = 'the'
print(poem.find(word))        #73
print(poem.rfind(word))       #214  (reverse find)
print(poem.count(word))       #3
print(poem.isalnum())         #False (only letters or numbers?)
```

Strip characters from string
```python
setup = '\na duck goes into a bar...'
print(setup.strip('.'))    #a duck goes into a bar
```

Capitalize all the words
```python
print(setup.title())       #A Duck Goes Into A Bar...
```

Capitalize all letters
```python
print(setup.upper())       #A DUCK GOES INTO A BAR...
```

Uncapitalize all letters
```python
print(setup.lower())       #a duck goes into a bar...
```

Swap upper and lower case
```python
print(setup.swapcase())    #A DUCK GOES INTO A BAR...'
```

Text alignment
```python
print(setup.center(30))    # center within 30 spaces
print(setup.rjust(30))     # right justify
print(setup.ljust(30))     # left justify
```

String replacement
```python
print(setup.replace('duck','marmoset'))
# a marmoset goes into a bar...
```

String replacement up to 100 times
```python
print(setup.replace('a ','a famous ', 100))
# a famous duck goes into a famous bar...
```

### Lists
```python
empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
```

You can also make an empty list with the list() function
```python
another_empty_list = list()
print(another_empty_list)   # []
```

Convert a string to a list
```python
print(list('cat'))   # ['c', 'a', 't']
```

Convert a tuple to a list
```python
a_tiple = ('ready', 'fire', 'aim')
print(list(a_tiple))
```
    ['ready', 'fire', 'aim']

Access/assign elements in a list
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])  #Groucho
print(marxes[-1]) #Harpo
marxes[2] = 'Wanda'
marxes;  #['Groucho', 'Chico', 'Wanda']
```

Lists of lists
```python
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'pigeon']
all_birds = [small_birds, extinct_birds, 'macaw']
all_birds; all_birds[0]; allbirds[1][0];
```
    [['hummingbird', 'finch'], ['dodo', 'pigeon'], 'macaw']
    ['hummingbird', 'finch']
    'dodo' 
    
Slicing
* think of indices as pointing between elements
```     +---+---+---+---+---+
     | A | b | c | d | e |
     +---+---+---+---+---+
     0   1   2   3   4   5
    -5  -4  -3  -2  -1
```
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0:2]   # ['Groucho', 'Chico']
marxes[::2]   # ['Groucho', 'Harpo']  (stepsize=2 right)
marxes[::-2]  # ['Harpo', 'Groucho']  (start at end and go left)
marxes[::-1]  # ['Harpo', 'Chico', 'Groucho']  (reverse the list)
```

Append single element to end of list
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo'); marxes
```
    ['Groucho', 'Chico', 'Harpo', 'Zeppo']

Append single element at specific point in list
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(3, 'Gummo'); marxes
marxes.insert(10, 'Karl'); marxes  # offset beyond end of list inserts at end
marxes.insert(0, 'Bobbo'); marxes  # offset 0 inserts at beginning of list
```
    ['Groucho', 'Chico', 'Gummo', 'Harpo']
    ['Groucho', 'Chico', 'Gummo', 'Harpo', 'Karl']
    ['Bobbo', 'Groucho', 'Chico', 'Gummo', 'Harpo', 'Karl']
   
Delete single element of a list   
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
del marxes[2]; marxes
del marxes[-1]; marxes
```
    ['Groucho', 'Chico', 'Gummo', 'Zeppo']
    ['Groucho', 'Chico', 'Gummo']

Delete single element of list by name
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo'); marxes
```
    ['Groucho', 'Chico', 'Harpo', 'Zeppo']
   
Get item from list and delete using pop()   
* note that `pop(0)` returns head of the list, `pop(-1)` returns tail
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()   # 'Zeppo'
marxes;        # ['Groucho', 'Chico', 'Harpo']
marxes.pop(1); # 'Chico'
marxes;        # ['Groucho', 'Harpo']
```
  
Get index of item in list by name
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico')  # 1
```
  
Combine/merge lists
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others); marxes;  # alternatively, marxes += others
```
    ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
    
Check for element in list
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes  # True
'Bob' in marxes      # False
```

Count occurances of element in a list
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.count('Harpo')  # 1
```

Convert elements of list to string
```python
marxes = ['Groucho', 'Chico', 'Harpo']
', '.join(marxes)  # 'Groucho, Chico, Harpo'
```

Sort a list
```python
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)  # creates a copy
sorted_marxes; # ['Chico', 'Groucho', 'Harpo']
marxes.sort()  # overwrites original list
marxes;        # ['Chico', 'Groucho', 'Harpo']
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)  # reverse sort
numbers;       # [4.0, 3, 2, 1]
```

Get length of list
```python
marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)  # 3
```

Copy a list
* note that if you just use `b=a` then `b` and `a` will point to the same object in memory, which you probably don't want
```python
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
```

### Tuples

* tuples are just immutable lists and elements that can't be added or deleted after the tuple is defined

```python
empty_tuple = ()
one_marx    = ('Groucho')                    # ('Groucho',)
marx_tuple  = ('Groucho', 'Chico', 'Harpo')  # ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a  # 'Groucho'
b  # 'Chico'
c  # 'Harpo'
```

Swap values/strings using tuples
```python
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
password  # 'tuttifrutti'
icecream  # 'swordfish'
```

Convert list to tuple
```python
marx_list  = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)  # ('Groucho', 'Chico', 'Harpo')
```

* _named_ tuples are a subclass of tuples that allow you to access values via `.name` as well as position via `[offset]`. They are similar to objects but are more space (and time) efficient
```python
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

duck
# Duck(bill='wide orange', tail='long')

duck.bill
# 'wide orange'
duck.tail
# 'long'

# you can make a named tuple from a dictionary
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)  # **parts is a keyword argument, which extracts the keys and values
                       # from the parts dictionary and supplies them as arguments to Duck()
duck2
# Duck(bill='wide orange', tail='long')

# named tuples are immutable; you have to define a new tuple to make a change
duck3 = duck2._replace(tail='magnificent', bill='crushing')
duck3
# Duck(bill='crushing', tail='magnificent')

# you can't add fields to a named tuple after it has been created
duck.color = 'green'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'color'
```

### Dictionaries

Converting tuples/lists to dictionaries
```python
# Convert a list (of two-item lists) to dict
alphabet1 = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
dict(alphabet1)  # {'c': 'd', 'a': 'b', 'e': 'f'}

# Convert a list (of two-item tuples) to dict
alphabet2 = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
dict(alphabet2)  # {'c': 'd', 'a': 'b', 'e': 'f'}

# Convert a tuple (of two-item lists) to dict
alphabet3 = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
dict(alphabet3)  # {'c': 'd', 'a': 'b', 'e': 'f'}

# Convert a tuple (of two-character strings) to dict
alphabet4 = [ 'ab', 'cd', 'ef' ]
dict(alphabet4)  # {'c': 'd', 'a': 'b', 'e': 'f'}

# Convert a list (of two-character strings) to dict
alphabet4 = ( 'ab', 'cd', 'ef' )
dict(alphabet4)  # {'c': 'd', 'a': 'b', 'e': 'f'}
```

Add or change item by key
```python
pythons = { 'Chapman':'Graham', 'Cleese':'John', 'Idle':'Eric', 'Jones':'Terry', 'Palin':'Michael', }
pythons['Gilliam'] = 'Gerry'  # add an item
pythons['Gilliam'] = 'Terry'  # change an item
pythons
```
    {'Cleese': 'John', 'Gilliam': 'Terry', 'Palin': 'Michael','Chapman': 'Graham', 'Idle': 'Eric', 'Jones': 'Terry'}

Repeated entries are clobbered
```python
pythons = {'Graham':'Chapman', 'John':'Cleese', 'Eric':'Idle', 'Terry':'Gilliam', 'Michael':'Palin', 'Terry':'Jones'}  # first Terry gets clobbered
pythons
```
    {'Terry':'Jones', 'Eric':'Idle', 'Graham':'Chapman', 'John':'Cleese', 'Michael':'Palin'}

Combine dictionaries
```python
pythons= { 'Chapman':'Graham', 'Cleese':'John', 'Gilliam':'Terry', 'Idle':'Eric', 'Jones':'Terry', 'Palin':'Michael', }
others = { 'Marx':'Groucho', 'Howard':'Moe' }
python.update(others)  # entries will be mixed together
```

Combining dictionaries with repeated entries will cause the second to overwrite the first
```python
first  = { 'a':1, 'b':2 }
second = { 'b':'platypus' }
first.update(second)
first  # { 'b':'platypus', 'a':1 }
```

Remove entries
```python
others = { 'Marx':'Groucho', 'Howard':'Moe' }
del others['Marx']

# remove all entries
others.clear()
others;  # {}
```

Test for a key in dictionaries
```python
others = { 'Marx':'Groucho', 'Howard':'Moe' }
'Marx' in python  # True
```

Get item in dictionary
```python
others = { 'Marx':'Groucho', 'Howard':'Moe' }
others.get('Marx', 'not in dict!')  # 'Groucho'
```

Get all keys in a dictionary
```python
letters = {'a':'b', 'c':'d', 'e':'f'}
letters.keys()        # dict_keys(['a', 'c', 'e'])
list(letters.keys())  # ['a', 'c', 'e']
```
Get all values in a dictionary
```python
letters = {'a':'b', 'c':'d', 'e':'f'}
list(letters.values())  # ['b', 'd', 'f']
```

Get all key-value pairs in a dictionary
```python
letters = {'a':'b', 'c':'d', 'e':'f'}
list(letters.items())  # [('a','b'), ('c','d'), ('e','f')]
```

Assigning and copying dictionaries
```python
# using = will create a pointer to the dictionary, basically
letters = {'a':'b', 'c':'d', 'e':'f'}
letters2 = letters
letters['g'] = 'h'
letters2  # {'a':'b', 'c':'d', 'e':'f', 'g':'h'}

# to actually copy a dictionary, use copy()
letters = {'a':'b', 'c':'d', 'e':'f'}
letters2 = letters.copy()
letters['g'] = 'h'
letters2  # {'a':'b', 'c':'d', 'e':'f'}
letters   # {'a':'b', 'c':'d', 'e':'f', 'g':'h'}
}
```

Handle missing keys with `setdefault()`
```python
# setdefault() is like get() except it assigns an item if the key is missing
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
# {'Helium': 2, 'Hydrogen': 1}

# if the key is not already in the dictionary then a new value is set
carbon = periodic_table.setdefault('Carbon', 12)
carbon 
# 12
periodic_table 
# {'Helium': 2, 'Carbon': 12, 'Hydrogen': 1}

# if the already exists in the dictionary then its original value is returned
helium = periodic_table.setdefault('Helium',947)
helium
# 2
periodic_table
# {'Helium': 2, 'Carbon': 12, 'Hydrogen': 1}
```

Handle missing keys with `defaultdict()`. It can accept the following:
`int`  -- returns 0
`list` -- return empty list ([])
`dict` -- return empty dictionary ({})
```python
# defaultdict() is similar to setdefault() but it sets a default for missing values
from collections import defaultdict
periodic_table = defaultdict(int)

# now any missing values will return a default value of 0
periodic_table['Hydrogen'] = 1
periodic_table['Lead']
# 0
periodic_table
# defaultdict(<class 'int'>, {'Lead': 0, 'Hydrogen': 1})

# an explicit example showing that the argument to defaultdict() must 
# be a function returning the value to be assigned to a missing key
from collections import defaultdict
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['A']
# 'Abominable Snowman'
bestiary['B'] 
# 'Basilisk'
bestiary['C']
# 'Huh?'

# an easier way
bestiary = defaultdict(lambda: 'Huh?')
bestiary('E')
# 'Huh?'
```

Create a dictionary that remembers the order of keys with `OrderedDict()`
```python
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

for stooge in quotes:
    print(stooge)
# Moe
# Larry
# Curly
```

### Sets

* sets are fundamentally just a sequence of values

Creating sets (sets are unsorted, like dictionary keys)
```python
empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
even_numbers # {0, 8, 2, 4, 6}
```

Convert string, list, tuple, dictionary to set (discards duplicates)
```python
letters = set('letters') # string to set
letters  # {'l','e','t','r','s'}
deers = set(['Dasher','Dancer','Prancer','Mason-Dixon']) # list to set
deers  # {'Dancer','Dasher','Prancer','Mason-Dixon'}
albums = set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') ) # tuple to set
albums  # {'Ummagumma','Atom Heart Mother','Echoes'}
colors = set( {'apple':'red', 'orange':'orange', 'cherry':'red'} ) # dict to set (values discarded)
colors  # {'apple','cherry','orange'}
```

Intersection, union, difference, xor, subset, proper subset
```python
a = {1,2}
b = {2,3}
a & b              # {2}  INTERSECTION
a.intersection(b)  # {2}  INTERSECTION
a | b              # {1,2,3}  UNION
a.union(b)         # {1,2,3}  UNION
a - b              # {1}  DIFFERENCE
a.difference(b)    # {1}  DIFFERENCE
a ^ b                   # {1,3}  XOR
a.symmetric_difference  # {1,3}  XOR
a <= b             # false  SUBSET
a.issubset(b)      # false  SUBSET
a < b              # false  PROPER SUBSET
a >= b             # false  SUPERSET
a.issuperset(b)    # false  SUPERSET
a > b              # false  PROPER SUPERSET
```

Test for values in a set
```python
# create a dict
drinks = {
...     'martini': {'vodka', 'vermouth'},
...     'black russian': {'vodka', 'kahlua'},
...     'white russian': {'cream', 'kahlua', 'vodka'},
...     'manhattan': {'rye', 'vermouth', 'bitters'},
...     'screwdriver': {'orange juice', 'vodka'}}

for name, contents in drinks.items():
        if 'vodka' in contents and not ('vermouth' in contents or
...        'cream' in contents):
            print(name)
# screwdriver
# black russian
```

Find common values in a set
```python
for name, contents in drinks.items():
        if contents & {'vermouth', 'orange juice'}
            print(name)
# screwdriver
# martini 
# manhattan

# exclude some values
for name, contents in drinks.items():
        if 'vodka' in contents and not contents & {'vermouth', 'cream'}
            print(name)
# screwdriver
# black russian
```

### Combining Data Structures

```python
# start with three lists
marxes  = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes,python,stooges
tuple_of_lists  # (['Groucho', 'Chico', 'Harpo'],['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'],['Moe', 'Curly', 'Larry'])

list_of_lists = [marxes, pythons, stooges]
list_of_lists  # [['Groucho', 'Chico', 'Harpo'],['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'],['Moe', 'Curly', 'Larry']]

dict_of_lists = {'Marxes':marxes, 'Pythons':pythons, 'Stooges':stooges}
dict_of_lists  # {'Stooges': ['Moe', 'Curly', 'Larry'],'Marxes': ['Groucho', 'Chico', 'Harpo'],'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']}
```

### If, While

Comparison operators
```python
==  !=  <  <=  >  >=
and  or  and not
```

Structures considered `false`
```python
False   # boolean
None    # null
0       # zero int
0.0     # zero float
''      # empty string
[]      # empty list
()      # empty tuple
{}      # empty dict
set()   # empty set
```

Example control structures
```python
mybool1 = True
mybool2 = True
color   = "red" 
if mybool:
    if mybool2:
        # do something
    elif color == "red":
        # do something else
    else:
        # do something else

count = 1
while count <=50
    # do something
    count += 1
    if count == 20
        continue
    print(count)
    if count == 49
        break
```

`while` with a "break checker"
```python
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Even number', number)
        break
    position += 1
else:  # break not encountered
    print('No even number found')
```

### For

Loop through iterable objects
```python
# list
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits:
    print(rabbit)
# Flopsy
# Mopsy
# Cottontail
# Peter

# string
word = 'cat'
for letter in word:
    print(letter)
# c
# a
# t

# dictionary
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation.keys:
    print(card)
# room
# weapon
# person

for value in accusation.values:
    print(value)
# ballroom
# lead pipe
# Col. Mustard

for item in accusation.items():
    print(item)
# ('room', 'ballroom')
# ('weapon', 'lead pipe')
# ('person', 'Col. Mustard')

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
# Card weapon has the contents lead pipe
# Card person has the contents Col. Mustard
# Card room has the contents ballroom
```

`for` with a "break checker"
```python
cheeses = []
for cheese in cheeses:
    print('Lovely', cheese)
    break
else:  # break not encountered
    print('No cheese available :(')
# No cheese available :(
```

### Zip

Iterate over multiple sequences in parallel (`zip` stops at the end of the shortest sequence)
```python
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts)
    print(day, drink, fruit, dessert)
# Monday coffee banana tiramisu
# Tuesday tea orange ice cream
# Wednesday beer peach pie
```

Combine sequences into a list or dictionary with `zip`
```python
english = 'Monday', 'Tuesday', 'Wednesday'
french  = 'Lundi', 'Mardi', 'Mercredi'

list(zip(english,french))
# [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]

dict(zip(english,french))
# {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}
```

### Ranges

Ranges of number can be generated with `range(start,stop,step)`
```python
range(0,3)          # 0, 1, 2
list(range(0,3))    # [0, 1, 2]
range(2,-1,-1)      # 2, 1, 0
list(range(0,11,2)) # [0, 2, 4, 6, 8, 10]
```

### List Comprehensions

```python
number_list = [number for number in range(1,6)]
number_list  # [1, 2, 3, 4, 5]

number_list = [number-1 for number in range(1,6)]
number_list  # [0, 1, 2, 3, 4]

a_list = [number for number in range(1,6) if number % 2 == 1]
a_list  # [1, 3, 5]

rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cells)
# (1, 1)
# (1, 2)
# (2, 1)
# (2, 2)
# (3, 1)
# (3, 2)

for row, col in cells:
    print(row, col)
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
```

### Dictionary Comprehensions

```python
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts  # {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
```

### Set Comprehensions

```python
a_set = {number for number in range(1,6) if number % 3 == 1}
a_set  # {1,4}
```

### Generator Comprehensions

```python
number_thing = ( number for number in range(1,6) ) # returns generator object

for number in number_thing:
    print number
# 1
# 2
# 3
# 4
# 5

number_list = list(number_thing)
number_list  # [1, 2, 3, 4, 5]
```

### Functions

Nested functions
```python
def knight(saying):
    def inner(quote):
        return "The knights say: '%s'" % quote
    return inner(saying)
    
knights('Ni!')
# "The knights say: 'Ni!'"
```

Keyword arguments can prevent positional argument confusion
```python
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
    
menu('beef', 'bagel', 'bordeaux') # bad
# {'dessert': 'bordeaux', 'wine': 'beef', 'entree': 'bagel'}

menu(entree='beef', dessert='bagel', wine='bordeaux') # good
# {'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}
```

Default parameters in functions
```python
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')
# {'dessert': 'pudding', 'wine': 'chardonnay', 'entree': 'chicken'}

menu('chardonnay', 'chicken', 'doughnut')
# {'dessert': 'doughnut', 'wine': 'chardonnay', 'entree': 'chicken'}
```

Gather multiple *positional* arguments with `*`
```python
# the asterisk groups a variable number of position arguments into a tuple
def print_args(*args):
    print('Positional argument tuple:', args)
    
print_args()
# Positional argument tuple: ()

print_args(3, 2, 1, 'go!')
# Positional argument tuple: ( 3, 2, 1, 'go!' )

def print_more(required1, required2, *args):
    print('Needed:', required1)
    print('Needed:', required2)
    print('All the rest:', args)
   
print_more('a', 'b', 'c', 'd', 'e')
# Needed: a
# Needed: b
# All the rest: ( 'c', 'd', 'e' )
```

Gather multiple *keyword* arguments with `**`
```python
# the double asterisk groups a variable number of keyword arguments into a dictionary
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
    # inside the function, kwargs is a dictionary
    
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# Keyword arguments: {'dessert': 'macaroon', 'wine': 'merlot', 'entree': 'mutton'}
```

Closures (dynamically-generated functions)
```python
def knight(saying):
    def inner():
        return "The knights say: '%s'" % saying
    return inner
    
a = knights('Duck')   # a new function called 'a'
b = knights('Goose')  # a new function called 'b'

a()
# "The knights say: 'Duck'"

b()
# "The knights say: 'Goose'"
```

Anonymous functions (`lambda()`)
```python
def edit_story(words, func):
    for word in words:
        print(func(word))

def enliven(word): 
    return word.capitalize() + '!'

stairs = ['thud', 'meow', 'thud', 'hiss']

edit_story(stairs, enliven)
# Thud!
# Meow!
# Thud!
# Hiss!

# alternatively, lambda() allows you to do it in one line:
edit_story(stairs, lambda word: word.capitalize() + '!')
# Thud!
# Meow!
# Thud!
# Hiss!
```

### Generator Function

Generators are sequence-creation objects
```python
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number  # note the yield instead of return
        number += step
        
# it's a normal function that returns a generator object
my_range                 # <function my_range at 0x10193e268>
ranger = my_range(1, 5)  # <generator object my_range at 0x101a0a168>

for x in range(1,5):
    print(x)
# 1
# 2
# 3
# 4

for x in ranger:
    print(x)
# 1
# 2
# 3
# 4
```

### Decorator Function

Decorators allow you modify a function without changing its source code (e.g. for debug purposes)
```python
# a simple debug decorator
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
    
def add_ints(a, b):
    return a+b

add_ints2 = document_it(add_ints)  # manual decorator assignment
add_ints2(3,5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 8

@document_it  # alternative decorator assignment
def add_ints3(a, b):
    return a + b
    
add_ints3(3, 5)
# Start function add_ints3
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 8

# you can have more than one decorator for a function
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# the decorator written closest to the function is run first
@document_it
@square_it
def add_ints4(a, b):
    return a + b
 
add_ints4(3,5)
# Running function: new_function
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 64
# 64

@square_it
@document_it
def add_ints5(a, b):
    return a + b
    
add_ints5(3,5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 64

 ```

### Namespaces

Namespaces are sections within which a particular name is unique
```python
# the main part of the program defines the global namespace
animal = 'fruitbat'
def print_global():
    # global variables can be called within functions
    print('inside print_global', animal)

print_global()
# inside_print_global: fruitbat

print('at the top level:', animal)
# at the top level: fruitbat

# you cannot both access a global variable and change it within the function
def change_and_print_global():
  print('inside change_and_print_global', animal)
  animal = 'wombat'  # ERROR
  print('after the change', animal) 

# if you *only* change a global variable then you essentially define a local variable
def change_local():
  animal = 'wombat'  # this one is defined in the function's local namespace
  print('inside change_local:', animal, id(animal))
  
change_local()
# inside change_local: wombat 4330406160

animal
# 'fruitbat'
id(animal)
# 4330390832 
```

If you don't say `global` within a function then variables are assumed to be in the function's local namespace
```python
# you can explicitly access a global variable inside a function
animal = 'fruitbat'
def change_and_print_global2():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global2', animal)
    
animal
# 'fruitbat'

change_and_print_global2()
# 'fruitbat'

animal
# 'wombat'
```

Global and local namespaces can be accessed using `globals()` and `locals()`
```python
animal = 'fruitbat'
def change_local():
  animal = 'wombat' # local variable
  print('locals:', locals())
  
animal
# 'fruitbat'

change_local()
# locals: {'animal': 'wombat'}

print('globals:',globals())
# globals: {'animal': 'fruitbat',
# '__doc__': None,
# 'change_local': <function change_it at 0x1006c0170>,
# '__package__': None,
# '__name__': '__main__',
# '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
# '__builtins__': <module 'builtins'>}

animal
# 'fruitbat'
```

### Exception Handling

A generic exception
```python
short_list = [1, 2, 3]
position = 5
short_list[position]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
```

`try` is run first; if an exception occurs then `except` is run
```python
short_list = [1, 2, 3]
position = 5
try: 
    short_list[position]
except:
    print('An exception occured')
# An exception occurred
```

You can also specify the exception type
```python
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)
        
# Position [q to quit]? 1
# 2
# Position [q to quit]? 0
# 1
# Position [q to quit]? 2
# 3
# Position [q to quit]? 3
# Bad index: 3
# Position [q to quit]? 2
# 3
# Position [q to quit]? two
# Something else broke: invalid literal for int() with base 10: 'two'
# Position [q to quit]? q
```

You can define your own exceptions
```python
# an exception is a class (a child of the class 'Exception')
class UppercaseException(Exception):
    pass  # let the parent class figure out what to print
    
words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
# Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
# __main__.UppercaseException: MO

# you can access the exception object itself and print it
try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)
# panic
```

### Creating Modules

A module called `report.py`:
```python
def get_description():  # note the docstring
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
```

The main program called `weatherman.py`:
```python
import report

description = report.get_description()  # a function within the module
print("Today's weather:", description)
```

Putting it together:
```python
$ python weatherman.py
Today's weather: who knows
$ python weatherman.py
Today's weather: sun
$ python weatherman.py
Today's weather: sleet
```

### Packages

If modules are properly organized in a subdirectory then Python can treat the subdirectory as a package. Note that you will also need a file `./sources/__init__.py` to exist so that Python knows the subdirectory is intended to be a package.

Main program: `./weather.py`
```python
from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
```

Module 1: `./sources/daily.py`
```python
def forecast():
    'fake daily forecast'
    return 'like yesterday'
```

Module 2: `./sources/weekly.py`
```python
def forecast():
    """Fake weekly forecast"""
    return ['snow', 'more snow', 'sleet', 'freezing rain', 'rain', 'fog', 'hail']
```

The result:
```python
$ python weather.py
Daily forecast: like yesterday
Weekly forecast:
1 snow
2 more snow
3 sleet
4 freezing rain
5 rain
6 fog
7 hail
```

### Objects

Creating the simplest classes
```python
# the simplest possible class
class Simplest():
    pass  # indicate the class is empty (just as we did w/ functions)
    
# create an object from a class
something = Simplest()
```

Creating a non-trivial class (note that `__init__` is a special function that initializes an individual object from its class definition; `self` specifies that it refers to the individual object itself)
The example below does the following:
1. looks up the definition of the `Person` class
2. creates a new object in memory
3. calls the object's `__init__` method, passing the newly-created object as `self` and the other argument as `name`
4. stores the value of `name` in the object
5. returns the object
```python
# a non-trivial class example. Note that __init__() is called
# automatically every time the class is used to create an object.
class Person():
    def __init__(self, name):
        self.name = name
    
# create an object for the Person class
hunter = Person('Elmer Fudd')    

print(hunter.name)
# Elmer Fudd
```

An illustration of how 'self' refers to the object being passed to the class
```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

car = Car()

# method 1 (the usual way)
car.exclaim()
# "I'm a Car!

# method 2 (the illustrative way)
Car.exclaim(car)
# "I'm a Car!
```

Inheritance
```python
# define a parent class
class Car():
    def exclaim(self):
        print("I'm a Car!")
        
# define a child class
class Yugo(Car):
    pass
    
give_me_a_car  = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
# I'm a Car!
give_me_a_yugo.exclaim()
# I'm a Car!
```

Overriding a method
```python
class Car():
    def exclaim(self):
        print("I'm a Car!")
        
# define a child class
class Yugo(Car):
    def exclaim(self):
        print("I'm not just any Car, I'm a Yugo!")
    
give_me_a_car  = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
# I'm a Car!
give_me_a_yugo.exclaim()
# I'm not just any Car, I'm a Yugo!!

# you can also override __init__()
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
        
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
        
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
# Fudd
print(doctor.name)
# Doctor Fudd
print(lawyer.name)
# Fudd, Esquire 
```

Adding a method to an inherited class
```python
class Car():
		def exclaim(self):
				print("I'm a Car!")

class Yugo(Car):
		def exclaim(self):
        print("I'm not just any Car, I'm a Yugo!")
		def need_a_push(self):
				print("A little help here?")

give_me_a_car  = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()
# A little help here?

give_me_a_car.need_a_push()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Car' object has no attribute 'need_a_push'
```

Call a parent class with `super()`. Note that when you define an `__init__()` method for a child class, you are replacing the `__init__` method of its parent class, so you need to call the parent one explicitly (i.e. it is not called automatically anymore)
```python
class Person():
		def __init__(self, name):
				self.name = name

class EmailPerson(Person):
		def __init__(self, name, email):
				super().__init__(name)
				self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
bob.name
# 'Bob Frapples'
bob.email
# 'bob@frapples.com'

# the following (without inheritance) would have also worked:
class EmailPerson2(Person):
		def __init__(self, name, email):
				self.name = name
				self.name = email
```

Note that all attributes and methods are public in Python and can be accessed directly, but you can also write _getters_ and _setters_ with `property` in Python (here the `name` property refers to a single attribute which we call `hidden_name` that is stored within the object)
```python
class Duck():
    # we don't want people to access the 'hidden_name' property directly (keep it private)...
    def __init__(self, input_name):
        self.hidden_name = input_name
    # ...so we define a getter and setter...
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    # ...and finally define the getter and setter as properies of the 'name' attribute
    # first argument to 'property' is the getter, second is the setter
    name = property(get_name, set_name)
        
# now whenever you refer to the 'name' of any 'Duck' object, it calls the getter 
fowl = Duck('Howard')
fowl.name
# inside the getter
# 'Howard'

# you can still use the getter like normal
fowl.get_name()
# inside the getter
# 'Howard'

# if you try to assign a value to the 'name' attribute, the setter is called
fowl.name = 'Daffy'
# inside the setter
fowl.name
# inside the getter
# 'Daffy'

# you can still use the setter like normal
fowl.set_name('Daffy')
# inside the setter
fowl.name
# inside the getter
# 'Daffy'
```

Properties can equivalently be defined with _decorators_
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property  # this one goes before the getter
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter  # this one goes before the setter
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
 
# note that now there are no visible get_name() or set_name() methods
fowl = Duck('Howard')
fowl.name
# inside the getter
# 'Howard'
fowl.name = 'Donald'
# inside the setter
fowl.name
# 'inside the getter'
# 'Donald'
```

We can also have a property return a _computed_ value instead
```python
class Circle():
    def __init__(self, radius):
        self.radius = radius
    # define a getter
    @property
    def diameter(self):
        return 2 * self.radius
        
# create a circle object with some radius
c = Circle(5)
c.radius
# 5

# we can refer to diameter as if it was an attibute like radius
c.diameter
#10

# changing the radius shows that diameter is a computed value
c.radius = 7
c.diameter
# 14

# note that we didn't define a setter so diameter is effectively read-only
c.diameter = 20
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute
```

In previous examples we called our hidden attribute `hidden_name`. We can instead use the Python naming convention for attributes that shouldn't be visible outside their class definition: two underscores `__`
```python
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    # define a getter
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    # define a setter
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

# all the old stuff still works
fowl = Duck('Howard')
fowl.name
# inside the getter
# 'Howard'
fowl.name = 'Donald'
# inside the setter
fowl.name
# 'inside the getter'
# 'Donald'

# now the __name attribute can't be directly accessed
fowl.__name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Duck' object has no attribute '__name'

# internally, the name has been mangled to make it unlikely for
# external code to access it, but here it is:
fowl._Duck__name 
# 'Donald'  # notice that it doesn't print 'inside the getter'
```

Class methods affect the class as a whole (any change you make affects all objects)
```python
# we define a class that counts how many object instances have been made from it
Class A():
    count = 0
    def __init__(self):
        # note we use A.count (class attribute) instead of self.count (object instance attribute)
        A.count += 1 
    def exclaim(self):
        print("I'm an A!")
    # we need a decorator to indicate that a function is a class method 
    @classmethod
    # the first parameter to a class method is the class itself (note that
    # the word 'class' is reserved so we use 'cls')
    def kids(cls):
        print("A has", cls.count, "objects.") # could have used A.count instead

easy_A = A()
breezy_A = A()
wheezy_A = A()
A.kids()
# A has 3 objects.
```

Static methods affect neither the class nor its objects
```python
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
    
CoyoteWeapon.commercial()
# This CoyoteWeapon has been brought to you by Acme
```

Polymorphism allows you to apply the same operation to different objects regardless of their class (also called _duck typing_: if it walks like a duck and quacks like a duck, it's a duck)
```python
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words  = words
    # return the value of the save 'person' string
    def who(self):
        return self.person
    # return the saved 'words' string with a period
    def says(self):
        return self.words + '.'
        
# note that __init__ is not redefined so Python calls the __init__ method of the parent class
# automatically to store 'person' and 'words', which is why we can access 'self.words'
class QuestionQuote(Quote):
    def says(self):  # redefine the says() method
        return self.words + '?'  
        
class ExclamationQuote(Quote):
    def says(self):  # redefine the says() method
        return self.words + '!'

# now illustrate that the three different says() methods provide different behaviour for
# the three classes (polymporphism)
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
# Elmer Fudd says: I'm hunting wabbits.

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
# Bugs Bunny says: What's up, doc?

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())
# Daffy Duck says: It's rabbit season!

# to illustrate polymorphism further, define a completely new class...
class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

#...and run the who() and says() methods of the various objects, even if
# they are completely unrelated to one another (polymorphism)
def who_says(obj):
    print(obj.who(), 'says', obj.says())
    
who_says(hunter)
# Elmer Fudd says I'm hunting wabbits.
who_says(hunted1)
# Bugs Bunny says What's up, doc?
who_says(hunted2)
# Daffy Duck says It's rabbit season!
who_says(brook)
# Brook says Babble
```

Special methods begin and end with two underscores
```python
# define a class that compares words and ignores case WITHOUT using special methods
class Word():
    def __init__(self, text):
        self.text = text
    
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
        
first = Word('ha')
second = Word('HA')
third = Word('eh')

first.equals(second)
# True
first.equals(third)
# False

# now do the same thing WITH using special methods (equality)
class Word2():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first2 = Word('ha')
second2 = Word('HA')
third2 = Word('eh')

first2 == second2
# True
first2 == third2
# False
```

Here is a list of common special methods:
```
__eq__(self,other)     self==other
__ne__(self,other)     self!=other
__lt__(self,other)     self<other
__gt__(self,other)     self>other
__le__(self,other)     self<=other
__ge__(self,other)     self>=other

__add__(self,other)        self+other
__sub__(self,other)        self-other
__mul__(self,other)        self*other
__floordiv__(self,other)   self//other
__truediv__(self,other)    self/other
__mod__(self,other)        self%other
__pow__(self,other)        self**other

__str__(self)          str(self)
__repr__(self)         repr(self)
__len__(self)          len(self)
```


An illustration of the `__str__()` and `__repr__()` special methods
```python
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("'  self.text  '")'
        
first = Word('ha')
first          # uses __repr__
# Word('ha')
print(first)   # uses __str__
```

Composition (aggregation) is better than inheritance when a child only needs a piece from the parent
```python
class Bill():
    def __init__(self, description):
        self.description = description
        
class Tail():
    def __init__(self, length):
        self.length = length
        
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')
        
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
# This duck has a wide orange bill and a long tail
```

### Code Checking with `pylint`

A script with an error
```python
a = 1
b = 2
print(a)
print(b)
print(c)
``` 

...then running `pylint` on it:
```
> pylint script.py
************* Module script
script.py:1:0: C0114: Missing module docstring (missing-module-docstring)
script.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
script.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
script.py:5:6: E0602: Undefined variable 'c' (undefined-variable)

------------------------------------
Your code has been rated at -6.00/10
```

Now fix it up:
```python
"Module docstring goes here!"

def func():
    "Function docstring goes here!"
    first  = 1
    second = 2
    third  = 3
    print(first)
    print(second)
    print(third)

func()
```

...then run `pylint` on it:
```
> pylint script.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: -6.00/10, +16.00)
```

### Testing with `unittest`

We will test a script `cap.py` that capitalizes all words in a string
```python
def just_do_it(text):
  return text.capitalize()
```

Now write a test script called `test_cap.py`
```python
import unittest
import cap

class TestCap(unittest.TestCase):
  
  # setUp() and tearDown() are called before each test method to
  # allocate/free resources, but not needed here
  def setUp(self):
    pass
  def tearDown(self):
    pass
    
  # the first test
  def test_one_word(self):
    text = 'duck'
    result = cap.just_do_it(text)
    self.assertEqual(result, 'Duck')
    
  # the second test 
  def test_multiple_words(self):
    text = 'a veritable flock of ducks'
    result = cap.just_do_it(text)
    self.assertEqual(result, 'A Veritable Flock Of Ducks')

if __name__ == '__main__':
  unittest.main()
```

Now run the test:
```
> python test_cap.py
F.
======================================================================
FAIL: test_multiple_words (__main__.TestCap)
----------------------------------------------------------------------
Traceback (most recent call last):
File "test_cap.py", line 23, in test_multiple_words
self.assertEqual(result, 'A Veritable Flock Of Ducks')
AssertionError: 'A veritable flock of ducks' != 'A Veritable Flock Of Ducks'
- A veritable flock of ducks
?   ^         ^     ^  ^
+ A Veritable Flock Of Ducks
?   ^         ^     ^  ^


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

Note that the test failed because the function `capitalize` only capitalizes the first letter of the first word. A better version would have `cap.py` like so:
```python
def just_do_it(text):
  from string import capwords
  return capwords(text)
```

Now run the test:
```python
> python test_cap.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### Logging Error Messages with `logging`

The logging levels and their numeric values are (default is `WARNING` 
* 0  `NOTSET`
* 10 `DEBUG`
* 20 `INFO`
* 30 `WARNING`
* 40 `ERROR`
* 50 `CRITICAL`

Basic logging functionality (output to file)
```python
import logging
logging.basicConfig(level='DEBUG', filename='out.log')

# create a logger object
logger = logging.getLogger('bunyan')

# write to the log at different levels
logger.debug("Where's my axe?")
logger.warning("I need my axe")
```

...and checking the output of `out.log`:
```
DEBUG:bunyan:Where's my axe?
WARNING:bunyan:I need my axe
```

### Miscellaneous

Grabbing command-line arguments
```python
import sys
print('Program arguments:', sys.argv)
```
```python
$ python test2.py
Program arguments: ['test2.py']
$ python test2.py tra la la
Program arguments: ['test2.py', 'tra', 'la', 'la']
```

Display the Python search path (note the empty line is an empty string `''` which represents the current directory)
```python
import sys
for place in sys.path:
    print(place)
#    
# /usr/lib/python38.zip
# /usr/lib/python3.8
# /usr/lib/python3.8/lib-dynload
# /usr/local/lib/python3.8/dist-packages
# /usr/lib/python3/dist-packages
```

Counting items in lists
```python
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter
# Counter({'spam': 3, 'eggs': 1})

# return all elements in descending order (or just the top n element)
breakfast_counter.most_common()
# [('spam', 3), ('eggs', 1)]
breakfast_counter.most_common(1) # n=1
# [('spam', 3)]

# you can combine counters
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter 
# Counter({'eggs': 2, 'bacon': 1})
breakfast_counter + lunch_counter
# Counter({'spam': 3, 'eggs': 3, 'bacon': 1})

# finding the symmetric difference of the counters
breakfast_counter - lunch_counter
# Counter({'spam': 3})
lunch_counter - breakfast_counter
# Counter({'bacon': 1, 'eggs': 1})

# finding the intersection of the counters
breakfast_counter & egg_counter
# Counter({'eggs': 1})  # note that the lower count is used

# find the union of the counters
breakfast_counter | lunch_counter
# Counter({'spam': 3, 'eggs': 2, 'bacon': 1})  # note that this doesn't add the counts
```

Working with a deque (deque = stack + queue, pronounced _deck_)
```python
def palindrome(word):
    from collections import deque
    dq=deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
    
palindrome('a')
# True
palindrome('racecar')
# True
palindrome('')
# True
palindrome('halibut')
# False
```

Iterate over code structures with `itertools`
```python
# run through all arguments as if they were a single iterable
import itertools  
for item in itertools.chain([1,2],['a','b']):
    print(item)
# 1
# 2
# a
# b

# infinitely cylcle through all arguments
for item in itertools.cycle([1,2]):
    print(item)
# 1
# 2
# 1
# 2
# ...

# calculate accumulated values
for item in itertools.accumulate([1,2,3,4]):
    print(item)
# 1
# 3
# 6
# 10

# you can customize the accumulate function behaviour
def multiply(a, b):
    return a * b
    
for item in itertools.accumulate([1,2,3,4], multiply): 
    print(item)
# 1
# 2
# 6
# 24
```

You can pretty print with `pprint()`
```python
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

pprint(quotes)
# {'Moe': 'A wise guy, huh?',
#  'Larry': 'Ow!',
#  'Curly': 'Nyuk nyuk!'}
```

Measure the runtime of a code snippet with `timeit`:
```python
from timeit import timeit
print(timeit('num = 5; num *= 2', number=1))
# 1.9020008039660752e-06

from timeit import repeat
print(repeat('num = 5; num *= 2', number=1, repeat=3))
# [1.691998477326706e-06, 4.070025170221925e-07, 2.4700057110749185e-07]
```

A more complicated `timeit` example:
```python
from timeit import timeit

# create a list by appending 1000 values
def make_list_1():
  result = []
  for value in range(1000):
    result.append(value)
  return result
  
# create a list by list comprehension
def make_list_2():
  result = [value for value in range(1000)]
  return result
  
print('make_list_1 takes', timeit(make_list_1, number=1000), 'seconds')
print('make_list_2 takes', timeit(make_list_2, number=1000), 'seconds')
# make_list_1 takes 0.14117428699682932 seconds
# make_list_2 takes 0.06174145900149597 second
```
