import os
from datetime import datetime
from time import sleep


def ft_progress(lst: list):
    """
    ETA: 8.67s [ 23%][=====>                  ] 233/1000 | elapsed time 2.33s
    """
    start = datetime.now()
    try:
        width, height = os.get_terminal_size()
    except:
        width, height = 0, 0
    last = len(lst)
    last_len = len(str(last))
    last_operation_durations = []
    for i in range(last):
        # Calculate estimated remaining time
        # last 100 times saved in last_operation_durations are in microseconds
        estimated = 0
        if last_operation_durations:
            estimated = ((sum(d / 1000000 for d in last_operation_durations) /
                         len(last_operation_durations))) * (last - i)
        diff = (datetime.now() - start)
        elapsed = diff.seconds + diff.microseconds / 1000000
        per_completion = (i + 1) / last
        # Calculate the number of bars out of the 24 bars
        bar_size = per_completion * 24
        bar_tip = '=' if i == last else '>'
        bar = '{:{bar_sep}>{bar_size}}{: <{bar_fill}}'.format(
            bar_tip, '', bar_sep='=', bar_size=bar_size, bar_fill=24 - bar_size)
        # Format the line before to pad with spaces
        # This is required to clear the terminal on smaller width after a longer width
        line = 'ETA: {:.2f}s [{:>4.0%}][{}] {:>{len_length}}/{} | elapsed time {:.2f}s'.format(
            estimated, per_completion, bar, i + 1, last, elapsed, len_length=last_len
        )
        line_end = '\n' if i == last else '\r'
        print('{: <{terminal_width}}'.format(
            line, terminal_width=width), end=line_end)
        operation_start = datetime.now()
        yield i
        # Save the last 100 operations duration to average them out
        last_operation_durations.append(
            (datetime.now() - operation_start).microseconds)
        if i > 100:
            last_operation_durations.pop(0)


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
