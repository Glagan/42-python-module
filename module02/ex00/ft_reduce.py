def ft_reduce(function_to_apply, iterable, initializer=None):
    if not callable(function_to_apply):
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
    iterator = iter(iterable)
    try:
        carry = next(iterator) if not initializer else initializer
    except StopIteration:
        raise TypeError("ft_reduce() of empty sequence with no initial value")
    for value in iterator:
        carry = function_to_apply(carry, value)
    return carry
