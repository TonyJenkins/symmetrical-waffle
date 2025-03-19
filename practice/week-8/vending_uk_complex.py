#!/usr/bin/env python3

def vending(cost, paid):
    if paid < cost:
        print("Insufficient funds.")
        return
    elif paid == cost:
        print("Thank you!!")
        return
    
    change_given = paid - cost
    print(f"The change to be dispensed is: {change_given} pence.")

    print(f"You will get: ")

    coin_list = [200, 100, 50, 20, 10, 5, 2, 1]
    for coin in coin_list:
        count = change_given // coin
        if count:
            print(f"{count} x {coin}p back")
            change_given %= coin

if __name__ == '__main__':
    try:
        cost = input("Enter the total cost of the item (in pence): ")
        paid = input("The amount paid (in pence): ")
        
        if not cost.isdigit() or not paid.isdigit():
            print("Invalid input, enter positive integer values only.")
        elif int(cost) <= 0 or int(paid) <= 0:
            print("Invalid input, cost and amount paid must be positive integers.")
        else:
            cost = int(cost)
            paid = int(paid)
            vending(cost, paid)
    except Exception as e:
        print("An error occurred:", e)
