import my_minipack.progressbar
import my_minipack.logger
from time import sleep


@my_minipack.logger.log
def ft_print(*args, **kwargs):
    print(*args, **kwargs)


ft_print('bouh', 'check machine.log')

listy = range(200)
ret = 0
for elem in my_minipack.progressbar.ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
