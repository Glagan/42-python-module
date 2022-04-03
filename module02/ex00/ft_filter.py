def ft_filter(function_to_apply, iterable):
    if not callable(function_to_apply):
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
    for item in iterable:
        if function_to_apply(item):
            yield item
