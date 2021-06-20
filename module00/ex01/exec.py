import sys

# slice -> [start:end:increment] with end not included
#                 reverse all characters               reverse and ignore first argv
#                 ^                                    ^
print(' '.join(arg[::-1].swapcase() for arg in sys.argv[:0:-1]))
