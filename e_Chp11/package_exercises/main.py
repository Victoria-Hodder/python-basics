from helpers.math import area
from helpers.string import shout

lengths = [5,6,7]
widths = [3,2,9]

for length, width in zip(lengths, widths):
    print(shout(f"the area of a {length} by {width} rectangle is {area(length, width)}"))
