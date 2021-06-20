import sys

if len(sys.argv) == 2:
    try:
        as_int = int(sys.argv[1])
        if as_int == 0:
            print("I'm Zero.")
        else:
            print("I'm {}.".format('Even' if as_int % 2 == 0 else 'Odd'))
    except:
        print('ERROR')
else:
    print('ERROR')