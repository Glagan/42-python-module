def what_are_the_vars(*args, **kwargs):
    result = ObjectC()
    for index, value in enumerate(args):
        setattr(result, 'var_{}'.format(index), value)
    for key, value in kwargs.items():
        if key in dir(result):
            return None
        setattr(result, key, value)
    return result


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    print("# Tests")

    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)

    print("\n# Scale")

    obj = what_are_the_vars(None)
    doom_printer(obj)
    # var_0: None
    # end

    obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
    doom_printer(obj)
    # function: <function what_are_the_vars at 0x...>
    # var_0: <function <lambda> at 0x...>
    # end

    obj = what_are_the_vars(3, var_0=2)
    doom_printer(obj)
    # ERROR
    # end
