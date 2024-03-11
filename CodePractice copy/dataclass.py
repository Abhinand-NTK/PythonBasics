# the below is the dataclasses in the python

from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str



# but in the traditional way it is like the below

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit



# Define a dataclass representing a Point with x and y coordinates
@dataclass
class Point:
    x: int  # Declare x coordinate as an integer
    y: int  # Declare y coordinate as an integer

# Create instances of the Point class
point1 = Point(3, 4)
point2 = Point(x=5, y=6)

# Print the instances
print("Point 1:", point1)
print("Point 2:", point2)

# Access attributes of the instances
print("x coordinate of Point 1:", point1.x)
print("y coordinate of Point 2:", point2.y)

# Compare instances for equality
print("Are Point 1 and Point 2 equal?", point1 == point2)

# Calculate hash values for the instances
print("Hash value of Point 1:", hash(point1))
print("Hash value of Point 2:", hash(point2))