"""
Threading is good for synchronous tasks
CPU bound tasks crunch numbers and use a lot of CPU
IO bound tasks wait for input and output operations to be completed (i.e downloading, network ops, read and write jobs)
"""

import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
