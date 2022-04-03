from NumPyCreator import NumPyCreator

npc = NumPyCreator()

print("\n# Tests")

print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
# Output:
# array([[1, 2, 3],
#        [6, 3, 4]])

print(npc.from_list([[1, 2, 3], [6, 4]]))
# Output
# None

lst = npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]])
print(lst, lst.dtype)
# Output
# array([['1', '2', '3'],
#        ['a', 'b', 'c'],
#        ['6','4','7']], dtype='< U21')

print(npc.from_list(((1, 2), (3, 4))))
# Output
# None

print(npc.from_tuple(("a", "b", "c")))
# Output
# array(['a', 'b', 'c'])

print(npc.from_tuple([[1, 2, 3], [6, 3, 4]]))
# Output
# None

print(npc.from_iterable(range(5)))
# Output
# array([0, 1, 2, 3, 4])

shape = (3, 5)
print(npc.from_shape(shape))
# Output
# array([[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]])

print(npc.random(shape))
# Output
# array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768],
#        [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
#        [0.79585328, 0.00660962, 0.92910958, 0.9905421, 0.05244791]])

print(npc.identity(4))
# Output
# array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])

print(npc.identity(0))
# Output
# array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])

print(npc.identity(-5))
# Output
# array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])

print("\n# Scale")

print(repr(npc.from_list([[], []])))
# array([], shape=(2, 0), dtype=float64)

print(repr(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6]])))
# array([[1, 2, 3],
#       [6, 3, 4],
#       [8, 5, 6]])

print(repr(npc.from_tuple(("a", "b", "c"))))
# array(['a', 'b', 'c'], dtype='<U1')

print(repr(npc.from_iterable(range(5))))
# array([0, 1, 2, 3, 4])

print(repr(npc.from_shape((0, 0))))
# array([], shape=(0, 0), dtype=float64)

print(npc.from_shape((3, 5)))
# array([[0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0.]])

print(npc.random((3, 5)))
# array([[0.74819604, 0.32295616, 0.27371925, 0.57171326, 0.92582071],
#       [0.70307642, 0.94846695, 0.12465384, 0.25146454, 0.11179953],
#       [0.38326719, 0.26179493, 0.88157011, 0.29978869, 0.72677049]])

print(npc.identity(4))
# array([[1., 0., 0., 0.],
#       [0., 1., 0., 0.],
#       [0., 0., 1., 0.],
#       [0., 0., 0., 1.]])

print("\nShould be None:")
print(npc.from_list("toto"))
print(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6, 7]]))
print(npc.from_tuple(3.2))
print(npc.from_tuple(((1, 5, 8), (7, 5))))
print(npc.from_shape((-1, -1)))
print(npc.identity(-1))
