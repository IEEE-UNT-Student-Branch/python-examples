""" Command Line """
# Output
print( "Output:" )
print( "Changing the 'end' value:" )
print( "line one", end=' ' )	# Expected output: 'line one line two'
print( "line two" )

print( "\nChanging the 'sep' value:" )
for i, a in enumerate( [ "Join", "UNT", "IEEE" ] ):
	print( i, a, sep='-->' )


# Input
print( "\n\nInput:" )
name = input( "What is your name?\n>>> " )
print( f"Hello, {name}!" )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" File """

file_name = "lorem_ipsum.txt"

'''
	Valid Modes:
		r	Reading (default). Synonym for 'rt'.
		w	Writing. Truncate the file first.
		x	Exclusive creation. Fails if the file exists.
		a	Writing. Append if the file exists.
		b	Binary mode.
		t	Text mode (default).
		+	Updating (reading and writing).
'''
# We're opening the file and storing it to the variable 'f'.
with open( "lorem_ipsum.txt", "r+" ) as f:
	contents = f.read()
	print( f"Original contents of {file_name}:\n{contents}" )

	# Go back to the beginning of the file.
	print( f"\nEnd of File: {f.tell() = }" )
	f.seek( 0, 0 )
	print( f"Beginning of File: {f.tell() = }" )

	# Iterate through each line of the file.
	# We use the single quotes to show that the newline is read in for each line.
	print( "\nEach line of the file:" )
	for l in list( f ):
		print( f"'{l}'", end='' )
	f.write( "\nAn appended line!\n" )

