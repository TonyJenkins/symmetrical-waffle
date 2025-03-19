#!/usr/bin/env python3

EXCHANGE_RATE = 1.3


if __name__ == '__main__':

    try:
        sterling = float(input('Enter amount in £: '))
    except ValueError:
        print('Error: must enter a number')
    else:
        if sterling >= 0:
            print(f'£{sterling:.2f} is equivalent to ${sterling * EXCHANGE_RATE:.2f}.')
        else:
            print('Error: cannot convert negative values.')
