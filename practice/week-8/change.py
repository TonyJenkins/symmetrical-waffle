#!/usr/bin/env python3

if __name__ == '__main__':

    try:
        price = int(input('Enter price (in pence):   '))
        payment = int(input('Enter payment (in pence): '))
    except ValueError:
        print('Error: integer required.')
    else:
        if payment <= 0 or price <= 0:
            print('Error: Negative values not allowed.')
        else:
            if payment >= price:
                change_due = payment - price
                if change_due == 0:
                    print('Exact amount paid. No change.')
                elif change_due >= 100:
                    print(f'Change due is £{(change_due / 100):.2f}.')
                else:
                    print(f'Change due is {change_due}p.')
            else:
                print('Error: not enough has been paid.')
