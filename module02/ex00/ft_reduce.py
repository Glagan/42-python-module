def ft_reduce(fct, iterable, initializer=None):
    if not callable(fct):
        raise TypeError("'{}' object is not callable".format(type(fct).__name__))
    iterator = iter(iterable)
    try:
        carry = next(iterator) if not initializer else initializer
    except StopIteration:
        raise TypeError("ft_reduce() of empty sequence with no initial value")
    for value in iterator:
        carry = fct(carry, value)
    return carry
