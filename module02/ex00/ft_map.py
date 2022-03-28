def ft_map(fct, *iterables):
    if not callable(fct):
        raise TypeError("'{}' object is not callable".format(type(fct).__name__))
    items = list(i.__iter__() for i in iterables)
    try:
        while True:
            args = []
            for i in items:
                args.append(next(i))
            yield fct(*args)
    except StopIteration:
        pass
