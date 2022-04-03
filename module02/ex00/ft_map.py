def ft_map(function_to_apply, iterable):
    if not callable(function_to_apply):
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
    try:
        for it in iterable:
            yield function_to_apply(it)
    except StopIteration:
        pass
