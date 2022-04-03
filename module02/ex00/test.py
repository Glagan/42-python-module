from functools import reduce
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

print("\n# Tests")

print("Success:")

# Example 1:
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
# Output:
# <generator object ft_map at 0x7f708faab7b0 >  # The adress will be different
print(list(ft_map(lambda t: t + 1, x)))
# Output:
# [2, 3, 4, 5, 6]

# Example 2:
print(ft_filter(lambda dum: not (dum % 2), x))
# Output:
# <generator object ft_filter at 0x7f709c777d00 >  # The adress will be different
print(list(ft_filter(lambda dum: not (dum % 2), x)))
# Output:
# [2, 4]

# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"

print("\nErrors:")

# Example 4:
lst = []
try:
    print(reduce(lambda u, v: u + v, lst))
except BaseException as err:
    print("(handled) {}".format(err))
try:
    print(ft_reduce(lambda u, v: u + v, lst))
except BaseException as err:
    print("(handled) {}".format(err))

# Example 8:
x = [1, 2, 3]
try:
    print(list(map("lol", x)))
except BaseException as err:
    print("(handled) {}".format(err))
try:
    print(list(ft_map("lol", x)))
except BaseException as err:
    print("(handled) {}".format(err))

# Example 9:
x = [1, 2, 3]
try:
    print(list(filter("lol", x)))
except BaseException as err:
    print("(handled) {}".format(err))
try:
    print(list(ft_filter("lol", x)))
except BaseException as err:
    print("(handled) {}".format(err))

# Example 10:


def test_raise(_):
    raise TypeError("lol")


x = [1, 2, 3]
try:
    print(list(map(test_raise, x)))
except BaseException as err:
    print("(handled) {}".format(err))
try:
    print(list(ft_map(test_raise, x)))
except BaseException as err:
    print("(handled) {}".format(err))

# Example 5:
x = []
print(list(filter(lambda dum: not (dum % 2), x)))
print(list(ft_filter(lambda dum: not (dum % 2), x)))

# Example 6:
x = []
print(list(map(lambda t: t + 1, x)))
print(list(ft_map(lambda t: t + 1, x)))

# Example 7:
x = [1, 2, 3]
try:
    print(list(map(lambda t: t + "aa", x)))
except BaseException as err:
    print("(handled) {}".format(err))
try:
    print(list(ft_map(lambda t: t + "aa", x)))
except BaseException as err:
    print("(handled) {}".format(err))


print("\n# Scale")


def function(x): return x + 1


iterable = [1, 2, 3]

print("\nft_map")

print(list(ft_map(lambda x: x + 2, [])))  # []
print(list(ft_map(lambda x: x + 2, [1])))  # [3]
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))  # [1, 4, 9, 16, 25]

# Expect <generator>
print(ft_map(function_to_apply=None, iterable=iterable))
# Expect TypeError
try:
    print(list(ft_map(function_to_apply=None, iterable=iterable)))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(list(ft_map(function_to_apply=2, iterable=iterable)))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(list(ft_map(function_to_apply=function, iterable=None)))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(list(ft_map(function_to_apply=function, iterable=2)))
except BaseException as err:
    print(err)


print("\nft_filter")

print(list(ft_filter(lambda x: x <= 1, [])))  # []

# Expect <generator>
print(ft_filter(function_to_apply=None, iterable=iterable))
# Expect TypeError
try:
    print(list(ft_filter(function_to_apply=None, iterable=iterable)))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(list(ft_filter(function_to_apply=2, iterable=iterable)))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(list(ft_filter(function_to_apply=function, iterable=None)))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(list(ft_filter(function_to_apply=function, iterable=2)))
except BaseException as err:
    print(err)

print("\nft_reduce")

print(ft_reduce((lambda x, y: x + y), [1]))  # 1
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))  # 24

# Expect None or Error
try:
    print(ft_reduce(None, iterable=iterable))
except BaseException as err:
    print(err)
# Expect None or Error
try:
    print(ft_reduce(2, iterable=iterable))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(ft_reduce(function, None))
except BaseException as err:
    print(err)
# Expect TypeError
try:
    print(ft_reduce(function, 2))
except BaseException as err:
    print(err)

#
