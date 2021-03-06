from vector import Vector

print('# Constructors')
print(repr(Vector(0)))
print(repr(Vector(6)))
print(repr(Vector((0, 0))))
print(repr(Vector((0, 10))))
print(repr(Vector((-5, 5))))
print(repr(Vector([])))
print(repr(Vector([0.0, 1.0, 2.0, 3.0])))
print(repr(Vector([[]])))
print(repr(Vector([[-3.0], [-2.0], [-1.0], [0.0]])))

print('\n# T')
v = Vector([[0.0], [1.0], [2.0], [3.0]])
print("v = {}".format(v))
print("v.shape = {}".format(v.shape))
print("v.T() = {}".format(v.T()))
print("v.T().shape = {}".format(v.T().shape))
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v2 = {}".format(v2))
print("v2.shape = {}".format(v2.shape))
print("v2.T() = {}".format(v2.T()))
print("v2.T().shape = {}".format(v2.T().shape))

print('\n# dot')
print("(0*0) + (1*1) + (2*2) + (3*3) = 14")
print("v.dot(v2.T()) = {}".format(v.dot(v2.T())))

v1 = Vector([0.0, 1.0, 2.0, 3.0])
print('\n## Scalar')
print('1 {}'.format(v1))
print('# Addition')
print('left', v1 + 1)
print('right', 1 + v1)
print('left', v1 + 2.5)
print('right', 2.5 + v1)
print('# Substraction')
print('left', v1 - 1)
print('right', 1 - v1)
print('left', v1 - 2.5)
print('right', 2.5 - v1)
print('# Multiplication')
print('left', v1 * 2)
print('right', 2 * v1)
print('left', v1 * 2.5)
print('right', 2.5 * v1)
print('# Division')
print('left', v1 / 2)
print('left', v1 / 2.5)
print('# Errors')
try:
    Vector([[-3.0, -2.0], [-2.0, -1.0], [-1.0, 0.0], [0.0, 1.0]])
except Exception as err:
    print(err)
try:
    v0 = Vector()
except Exception as err:
    print(err)
try:
    v0 = Vector(-1)
except Exception as err:
    print(err)
try:
    v0 = Vector(12.0)
except Exception as err:
    print(err)
try:
    v0 = Vector('vector')
except Exception as err:
    print(err)
try:
    v0 = Vector((12, 6))
except Exception as err:
    print(err)
try:
    v0 = Vector((12))
except Exception as err:
    print(err)
try:
    v0 = Vector(('min'))
except Exception as err:
    print(err)
try:
    v0 = Vector(('min', 'max'))
except Exception as err:
    print(err)
try:
    v0 = Vector([12])
except Exception as err:
    print(err)
try:
    v0 = Vector(['quarante-deux'])
except Exception as err:
    print(err)
try:
    v0 = Vector([12.0, 'quarante-deux', 6.0])
except Exception as err:
    print(err)
try:
    print(2 / v1)
except Exception as err:
    print(err)
try:
    print(2.5 / v1)
except Exception as err:
    print(err)
try:
    print(v1 / 0)
except Exception as err:
    print(err)
try:
    print(v1 / 0.0)
except Exception as err:
    print(err)

v2 = Vector([0.0, 2.0, 4.0, 6.0])
v3 = Vector([-1.0, 1.0])
print('\n## Vector')
print('1 {}'.format(v1))
print('2 {}'.format(v2))
print('# Addition')
print(v1 + v2)
print(v2 + v1)
print('# Substraction')
print(v1 - v2)
print(v2 - v1)
print('# Multiplication')
print(v1 * v2)
print(v2 * v1)
print('# Errors')
print('3 {}'.format(v3))
try:
    print(v1 + v3)
except Exception as err:
    print(err)
try:
    print(v3 + v1)
except Exception as err:
    print(err)
try:
    print(v1 - v3)
except Exception as err:
    print(err)
try:
    print(v3 - v1)
except Exception as err:
    print(err)
try:
    print(v1 * v3)
except Exception as err:
    print(err)
try:
    print(v3 * v1)
except Exception as err:
    print(err)
