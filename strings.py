# the print() function adds spaces between strings, and a newline at the end
print(99,'bottles','would be enough.\n') 
#99 bottles would be enough

# strings can be enclosed by either single or double quotes
a = 'snap'; print(a)            #snap
b = "crackle"; print(b,'\n')    #crackle

# you can combine quotes so that strings can contain ' or "
c = "and I said 'nay' to him"; print(c)     
d = 'a captive double quote (")'; print(d)
#and I said 'nay' to him 
#a captive double quote (") 

# you can also just use escape characters
esc = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(esc)
#"I did nothing!" he said. "Not that either! Or the other thing."

# triple quotes are useful for multiline strings without having to use \n
# (note that if you had used single quotes here, you would get an EOL error)
multi = '''
Here is a multiline string
containing a double quote (")
'''; print(multi)
#Here is a multiline string
#containing a double quote (")

# empty strings can be created in a number of ways
e = ''; 
f = ""; 
g = ''''''; 
h = """"""; 

# note that Python does not add spaces when concatenating strings,
# but the print() function does!
duck  = 'Duck.'
goose = 'Goose.'
print(duck + duck + goose)
print(duck,duck,goose)
#Duck.Duck.Goose.
#Duck. Duck. Goose.

# blank strings are useful as a starting point for concatenation
bottles = 99
base    = ''
base   += 'current inventory: '
base   += str(bottles)
print(base, '\n')
#current inventory: 99

# you can duplicate strings with *
start = 'Na' * 8
end   = 'Batman!'
print(start,end,'\n')
#NaNaNaNaNaNaNaNa Batman!

# you can extract a character from a string by specifying its offset, or slicing
# syntax is [start:end:step]
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])      #a
print(letters[-1])     #z
print(letters[11:15])  #lmno
print(letters[22:])    #wxyz
print(letters[-4:])    #wxyz
print(letters[22:-1])  #wxy
print(letters[22:-10]) #empty string!
print(letters[::7])    #ahov; start to end in steps of 7
print(letters[::-1])   #backwards! zyxwvutsrqponmlkjihgfedcba

# you can split strings quite easily
todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(',')) # split by commas
#['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']
print(todos.split())    # default is to split by spaces
#['get', 'gloves,get', 'mask,give', 'cat', 'vitamins,call', 'ambulance']

# note the split behaviour for repeating separator strings
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
#['a', 'b', '', 'c', 'd', '', '', 'e']
print(splitme.split('//'))
#['a/b', 'c/d', '/e']

# how to join lists into a single string
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('\nFound and signing book deals:', crypto_string)
#Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

# how to create a paragraph out of a list
para = ['line 1', 'line 2', 'line 3']
para_string = '\n'.join(para)
print(para_string)
#line 1
#line 2
#line 3

# illustrating some general string functions
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

# strip characters from string
setup = '\na duck goes into a bar...'
print(setup.strip('.'))    #a duck goes into a bar
  
# capitalize all the words
print(setup.title())       #A Duck Goes Into A Bar...

# capitalize all letters
print(setup.upper())       #A DUCK GOES INTO A BAR...

# uncapitalize all letters
print(setup.lower())       #a duck foes into a bar...

# swap upper and lower case
print(setup.swapcase())    #A DUCK GOES INTO A BAR...'

# text alignment
print(setup.center(30))    # center within 30 spaces
print(setup.rjust(30))     # right justify
print(setup.ljust(30))     # left justify

# string replacement
print(setup.replace('duck','marmoset'))
#a marmoset goes into a bar...

# string replacement up to 100 times
print(setup.replace('a ','a famous ', 100))
#a famous duck goes into a famous bar...
