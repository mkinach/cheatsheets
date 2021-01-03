# Git Cheatsheet
#### References:

These notes came from the following sources:

    INTRODUCING PYTHON (1st Edition)
    Bill Lubanovic
    O'Reilly 2015

### Strings

The `print()` function adds spaces between strings, and a newline at the end
```python
print(99,'bottles','would be enough.\n') 
```
    99 bottles would be enough

Strings can be enclosed by either single or double quotes
```python
a = 'snap'; print(a)            #snap
b = "crackle"; print(b,'\n')    #crackle
```

You can combine quotes so that strings can contain ' or "
```python
c = "and I said 'nay' to him"; print(c)     
d = 'a captive double quote (")'; print(d)
```
    and I said 'nay' to him 
    a captive double quote (") 

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
print(setup.lower())       #a duck foes into a bar...
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

### Define some lists
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

Access elements in a list
```python
marxes = ['Grucho', 'Chico', 'Harpo']
print(marxes[0])  #Groucho
print(marxes[-1]) #Harpo
```
