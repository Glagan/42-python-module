def ft_filter(fct, iterable):
    if not callable(fct):
        raise TypeError("'{}' object is not callable".format(type(fct).__name__))
    for item in iterable:
        if fct(item):
            yield item
