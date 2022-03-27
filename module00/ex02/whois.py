import sys

try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert sys.argv[1].isnumeric(), "argument is not an integer"
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    else:
        print("I'm {}.".format('Even' if number % 2 == 0 else 'Odd'))
except AssertionError as err:
    print("Assertion error: {}".format(err))
