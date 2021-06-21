from vector import Vector

print('# Constructors')
print(repr(Vector(0)))
print(repr(Vector(6)))
print(repr(Vector((0, 10))))
print(repr(Vector((-5, 5))))
print(repr(Vector([])))
print(repr(Vector([0.0, 1.0, 2.0, 3.0])))
print(repr(Vector([-3.0, -2.0, -1.0, 0.0])))

v1 = Vector([0.0, 1.0, 2.0, 3.0])
print('## Scalar')
print('1 {}'.format(v1))
print('# Addition')
print(v1 + 1)
print(1 + v1)
print(v1 + 2.5)
print(2.5 + v1)
print('# Substraction')
print(v1 - 1)
print(1 - v1)
print(v1 - 2.5)
print(2.5 - v1)
print('# Multiplication')
print(v1 * 2)
print(2 * v1)
print(v1 * 2.5)
print(2.5 * v1)
print('# Division')
print(v1 / 2)
print(v1 / 2.5)
print('# Errors')
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
print('## Vector')
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
