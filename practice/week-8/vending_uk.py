
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

  coin_list = [200, 100, 50, 20, 10, 5, 2, 1]
  for coin in coin_list:
    count = change_given // coin
    if count:
      print(f"You will get {count} x {coin}p return")
      change_given %= coin

if __name__ == '__main__':
    
    cost = int(input("Enter the total cost of the item (in pence): "))
    paid = int(input("The amount paid (in pence): "))
    
    vending(cost, paid)