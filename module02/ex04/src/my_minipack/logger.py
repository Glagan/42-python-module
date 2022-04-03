import os
from functools import wraps
from datetime import datetime


def log(fct):
    @wraps(fct)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = fct(*args, **kwargs)
        total = (datetime.now() - start)
        with open('machine.log', 'a') as log_file:
            if total.total_seconds() >= 1:
                total_str = '{:<4.3f} s '.format(total.total_seconds())
            else:
                total_str = '{:<4.3f} ms'.format(total.microseconds / 1000)
            line = '({})Running: {:<18} [ exec-time = {} ]\n'
            log_file.write(line.format(os.environ["USER"], ' '.join(
                fct.__name__.split('_')).title(), total_str))
        return result
    return wrapper
