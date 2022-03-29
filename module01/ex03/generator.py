from random import randint


def generator(text: str, sep: str = " ", option: str = None) -> str:
    """
    Option is an optional arg, sep is mandatory
    """
    if not isinstance(text, str):
        print('ERROR')
        return
    if option is not None and option not in ["shuffle", "ordered", "unique"]:
        print('ERROR')
        return
    try:
        lst = text.split(sep)
    except BaseException:
        return None
    if option == "shuffle":
        tmp = []
        for i in range(len(lst)):
            tmp.append(lst.pop(randint(0, len(lst) - 1)))
        lst = tmp
    elif option == "ordered":
        lst.sort()
    elif option == "unique":
        lst = list(set(lst))
    for word in lst:
        yield word


if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."
    print(text)
    for word in generator(text, sep=" "):
        print(word)
    print()

    print("shuffle:", text)
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print()

    print("ordered:", text)
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print()

    text = "Lorem Ipsum Lorem Ipsum"
    print("unique:", text)
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print()

    text = 1.0
    print(text)
    for word in generator(text, sep="."):
        print(word)
