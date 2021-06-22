def ft_map(fct, *iterables):
    class FtMap:
        def __init__(self, fct, *iterables):
            self.fct = fct
            self.iterables = iterables
            self.iterators = list(i.__iter__() for i in iterables)

        def __iter__(self):
            return self

        def __next__(self):
            args = []
            for i in self.iterators:
                args.append(next(i))
            return self.fct(*args)

    return FtMap(fct, *iterables)
