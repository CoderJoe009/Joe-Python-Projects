coins = [5,10,25]
total = 50
def main():
    print(f"Amount Due: {total}")
    pay(total)


def pay(rem):

    while rem > 0:
        coin = int(input("Insert Coin:").strip())
        if coin not in coins:
            print("Amount Due:",total)
        elif coin in coins:
            rem = process(coin, rem)


def process(coin, remaining_cost):
   rem = remaining_cost - coin
   if rem <= 0:
        print(f"Change Owed: {rem}")
   if rem > 0:
        print(f"Amount Due: {rem}")
   return rem


main()
