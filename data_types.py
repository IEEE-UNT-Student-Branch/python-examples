""" Numerical """
print( "Numerical Types:" )

# int
n = i = j = 2	# You can assign multiple variables to the same value at the same time.
print( f"\tInteger:\n\t\t{n = }\n\t\t{type(n) = }" )


# float
f = 3.1415		# To define a float, all you need is a decimal point. You don't need values afterwards (e.g., 3.).
print( f"\tReal/Float:\n\t\t{f = :0.2f}\n\t\t{type(f) = }" )


# bool
b = True		# Either true or false.
print( f"\tBoolean:\n\t\t{b=}\n\t\t{type(b) = }" )


# complex
c = ( 2.3 + 5.6j )	# You don't need the parenthesis to define a complex number.
print( f"\tComplex:\n\t\t{c=}\n\t\t{type(c) = }" )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Sequences """
print( "\n\nSequence Types:" )

# str
s = "Join IEEE!"
print( f"\tString:\n\t\t{s = }\n\t\t{s[5:] = }\n\t\t{type(s) = }" )		# Notice how the string is indexed using square brackets.


# tuple
t = ( "and", "RAS" )
print( f"\tTuple:\n\t\t{t=}\n\t\t{type(t) = }" )


# list
l = [ 1, 3, "apple", 3.6, ( "a", "tuple" ) ]

print( f"\tList:\n\t\t{l = }\n\t\t{len(l) = }", end='\n\t\t' )

for item in l:							# Iterating through each item in the list.
	print( f"{item}", end=', ' )
print( "\n", end='\n\t\t' )

l = [ x ** 2 for x in range( 10 ) ]		# Using list comprehension to create squares through 81.

for index, item in enumerate( l ):		# Enumerating the list to get the index and value.
	print( index, item, end='\n\t\t', sep=' - ' )
print( f"{type(l) = }" )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Mappings """
print( "\n\nMappings:" )

# dict
d = { "a" : 0.9, "b" : 0.05, "c" : 0.05 }

print( f"\tDictionary:\n\t\t{dict = }", end='\n\t\t' )	# Notice that printing the variable doesn't show the values.
for k, v in d.items():									# Iterating through each key-value pair.
	print( k, v, end='\n\t\t', sep=' : ' )
print( f"{d[ 'a'] = }\n\t\t{type(d) = }" )

