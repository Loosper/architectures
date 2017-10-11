#! /usr/bin/env python3
import sys
import os


def get_str(num):
    pin = str(num)
    return (3 - len(pin)) * ' ' + pin


def print_index(index):
    print(' ' * 4, ' '.join(
            [get_str(index(i)) for i in range(len(buf[0]))]
        ),
        sep=''
    )


def print_buffer(buf, x=-1, y=-1):
    # top row
    print_index(lambda i: '1' if i != y - len(buf) else '0')

    for index, line in enumerate(buf):
        string = ''
        for row in line:
            string += '| {} '.format(row)

        # side row
        print(
            get_str(index),
            string + '|' + get_str('0' if index != x else '1') + '\n',
            '   ',  '_' * len(buf[0]) * 4, sep=''
        )

    # bottom row
    print_index(lambda i: i + len(buf))


if len(sys.argv) < 3:
    # argparse is the tool, but for just 2 paramteres is not needed
    print('Usage: {} [x] [y]'.format(sys.argv[0]))
    exit()

x = int(sys.argv[1])
y = int(sys.argv[2])

# x - diode backward
# o - diode forward
buf = [['x' for _ in range(y)] for _ in range(x)]

print_buffer(buf)

while True:
    pins = input()
    new_x, new_y = [int(i) for i in pins.split()]

    buf[new_x][new_y - x] = 'o'
    os.system('clear')
    print_buffer(buf, new_x, new_y)
    buf[new_x][new_y - x] = 'x'
