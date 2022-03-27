def text_analyzer(string=False, *args, **kwargs) -> None:
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if args or kwargs:
        print('Too many arguments')
        return
    if string is False:
        string = str(input("What is the text to analyse?\n"))
    if not isinstance(string, str):
        print('The text should be a string')
        return
    count = {'upper': 0, 'lower': 0, 'punctuation': 0, 'spaces': 0}
    for c in string:
        if c.isspace():
            count['spaces'] += 1
        elif c.isupper():
            count['upper'] += 1
        elif c.islower():
            count['lower'] += 1
        elif not c.isalnum():
            count['punctuation'] += 1
    print('The text contains {} characters:'.format(len(string)))
    print('- {} upper letters'.format(count['upper']))
    print('- {} lower letters'.format(count['lower']))
    print('- {} punctuation marks'.format(count['punctuation']))
    print('- {} spaces'.format(count['spaces']))
