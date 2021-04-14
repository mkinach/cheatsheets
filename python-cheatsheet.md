# Python 3 Cheatsheet
#### References:

These notes came from the following sources:

    INTRODUCING PYTHON (1st Edition)
    Bill Lubanovic
    O'Reilly 2015

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
```
    "I did nothing!" he said. "Not that either! Or the other thing."

Triple quotes are useful for multiline strings without having to use \n (note that if you had used single quotes here, you would get an EOL error)
```python
multi = '''
Here is a multiline string
containing a double quote (")
'''; print(multi)
```
    Here is a multiline string
    containing a double quote (")

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
```
    Duck.Duck.Goose.
    Duck. Duck. Goose.

Blank strings are useful as a starting point for concatenation
```python
bottles = 99
base    = ''
base   += 'current inventory: '
base   += str(bottles)
print(base, '\n')
```
    current inventory: 99

You can duplicate strings with *
```python
start = 'Na' * 8
end   = 'Batman!'
print(start,end,'\n')
```
    NaNaNaNaNaNaNaNa Batman!

Yyou can extract a character from a string by specifying its offset, or slicing. The syntax is `[start:end:step]`
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

You can split strings quite easily
```python
todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(',')) # split by commas
```
    ['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']
```python
print(todos.split())    # default is to split by spaces
```
    ['get', 'gloves,get', 'mask,give', 'cat', 'vitamins,call', 'ambulance']

Note the split behaviour for repeating separator strings
```python
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
```
    ['a', 'b', '', 'c', 'd', '', '', 'e']
```python
print(splitme.split('//'))
```
    ['a/b', 'c/d', '/e']

How to join lists into a single string
```python
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('\nFound and signing book deals:', crypto_string)
```
    Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

How to create a paragraph out of a list
```python
para = ['line 1', 'line 2', 'line 3']
para_string = '\n'.join(para)
print(para_string)
```
	  line 1
	  line 2
	  line 3

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
```
    a marmoset goes into a bar...

String replacement up to 100 times
```python
print(setup.replace('a ','a famous ', 100))
```
    a famous duck goes into a famous bar...

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

* tuples are just immutable lists and elements can't be added or deleted after the tuple is defined

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
