import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()

arr1 = np.arange(0, 25).reshape(5, 5)
print("crop", spb.crop(arr1, (3, 1), (1, 0)))
# Output
# array([[5],
#        [10],
#        [15]])

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print("thin", spb.thin(arr2, 3, 0))
# Output
# array([['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')

arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
print("thin", spb.thin(arr3, 3, 1))
# Output
# array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
#       ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
#       ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
#       ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
#       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("juxtapose", spb.juxtapose(arr4, 2, 0))
# Output
# array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9],
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])

arr5 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print("mosaic 2,2", spb.mosaic(arr5, (2, 2)))
print("mosaic 1,1", spb.mosaic(arr5, (1, 1)))
print("mosaic 1,5", spb.mosaic(arr5, (1, 5)))

print("\nShould be None:")
not_numpy_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spb.crop(not_numpy_arr, (1, 2)))
print(spb.juxtapose(arr4, -2, 0))
print(spb.mosaic(arr4, (1, 2, 3)))
