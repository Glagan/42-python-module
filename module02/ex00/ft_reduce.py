def ft_reduce(fct, iterable, initializer=None):
    iterator = iter(iterable)
    carry = next(iterator) if not initializer else initializer
    for value in iterator:
        carry = fct(carry, value)
    return carry
