def ft_filter(fct, iterable):
    class FtFilter:
        def __init__(self, fct, iterable):
            self.fct = fct
            self.iterable = iterable
            self.iterator = self.iterable.__iter__()

        def __iter__(self):
            return self

        def __next__(self):
            while True:
                arg = next(self.iterator)
                if self.fct == None:
                    if arg:
                        return arg
                elif self.fct(arg):
                    return arg

    return FtFilter(fct, iterable)
