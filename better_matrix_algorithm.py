#! /usr/bin/env python3
import sys
import os


def get_str(num):
    pin = str(num)
    return (3 - len(pin)) * ' ' + pin


def print_buffer(buf, x=-1, y=-1):
    def estimate(index):
        # OPTIMISATION: do not set wires to H if not necessary
        # because it's quite likely that 1 of the wires will aready be at
        # 1 or 0 and setting to H is a VERY slow process

        to_print = 'H'
        if index == x:
            to_print = '0'
        elif index == y - len(buf):
            to_print = '1'
        return to_print

    for index, line in enumerate(buf):
        string = ''
        for row in line:
            string += '| {} '.format(row)

        # 0 - signal 0
        # 1 - signal 1
        # H - high resistance
        print(
            get_str(index),
            string + '|' + get_str(estimate(index)) + '\n',
            '   ',  '_' * len(buf[0]) * 4, sep=''
        )

    print(' ' * 4, ' '.join(
            [get_str(i + len(buf)) for i in range(len(buf[0]))]
        ),
        sep=''
    )


if len(sys.argv) < 2:
    # argparse is the tool, but for just 1 paramter is not needed
    print('Usage: {} [size]'.format(sys.argv[0]))
    exit()

y = x = int(sys.argv[1])

# x - diode backward
# o - diode forward
# r - resistor
buf = [['x' if a != b else 'r' for b in range(y)] for a in range(x)]

print_buffer(buf)

while True:
    pins = input()
    new_x, new_y = [int(i) for i in pins.split()]
    if new_x == new_y - x:
        continue

    buf[new_x][new_y - x] = 'o'
    os.system('clear')

    print_buffer(buf, new_x, new_y)
    buf[new_x][new_y - x] = 'x'
