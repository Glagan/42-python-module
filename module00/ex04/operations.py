import sys


def show_help() -> None:
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('\tpython operations.py 10 3')
    exit()


argc = len(sys.argv)
number1 = False
number2 = False

if argc > 3:
    print('InputError: too many arguments')
    show_help()
elif argc == 2:
    print('InputError: too little arguments')
    show_help()
elif argc != 3:
    show_help()

try:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
except:
    print('InputError: only numbers')
    show_help()

results = {'Sum': False, 'Difference': False,
           'Product': False, 'Quotient': False, 'Remainder': False}
results['Sum'] = number1 + number2
results['Difference'] = number1 - number2
results['Product'] = number1 * number2
if number2 == 0:
    results['Quotient'] = 'ERROR (div by zero)'
    results['Remainder'] = 'ERROR (modulo by zero)'
else:
    results['Quotient'] = number1 / number2
    results['Remainder'] = number1 % number2

for k, v in results.items():
    #                    adjust to the longest
    #                              v
    print('{} {}'.format((k + ':').ljust(12), v))
