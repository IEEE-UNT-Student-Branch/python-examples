""" Comments """
# Single line comment

"""
    Multi-line docstring using double quotes
"""

'''
    Multi-line comment using single quotes
'''

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Indentation """
# Blocks
for a in range(5):
    pass

# Line Joining
print("Line Joining:")
print("Multiple " + \
      "Lines")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Control Loops """
# if, elif, else
a = 10
b = 10
x = 10
y = 12

print("\nif, elif, else:")

if a < b:
    print(f"{a < b = }")
elif a > b:
    print(f"{a > b = }")
else:
    print(f"{a == b = }")

if x == 10 and y == 10:  # Use and, or, and not for boolean comparisons.
    print("x == y == 10")

# for
print("\nfor:")
l = [1, 2, 4]
for d in l:
    if d == 3:
        print("Item found!")
        break
else:  # This statement only runs if the loop exits successfully (did not break out).
    print("Item not found!")

# while
print("while:")
while a > 0:
    print(a, end=' ')
    a = a - 1

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Functions """

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                            # 1 positional argument
parrot(voltage=1000)                                    # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')           # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword

# These are all invalid calls. Uncomment them to see the errors.
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Classes """
class Vehicle:
    """docstring"""

    # This is the constructor that is called when creating a new instance of this class.
    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color  # We use the self object to access the object's attributes and methods.
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"


myCar = Vehicle( "Blue", 4, 4 ) # Create a new instance of the Vehicle class. Notice we don't send the 'self' parameter.



