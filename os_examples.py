import os

print( f"{os.name = }" )

print( f"\nPath:\n{os.path.exists( '../' ) = }" )	# '../' goes up one directory level.
print( f"{os.path.isdir( '../' ) = }" )
print( f"{os.path.isfile( '../' ) = }" )
print( f"\nCheck the current directory and move it:\n{os.getcwd() = }" )
print( f"{os.chdir( '../' )}" )
print( f"{os.getcwd() = }" )

