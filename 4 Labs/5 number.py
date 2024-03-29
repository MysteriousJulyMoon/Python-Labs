n = int(input("Enter the number of entries: "))  #Ввод количества записей
purchases = {}

for _ in range(n):
    buyer_id, item, quantity = input("Enter the Buyer's ID, product and quantity separated by a space: ").split()  #Ввод ID Покупателя, товара и кол-ва
    quantity = int(quantity)

    if buyer_id in purchases:
        if item in purchases[buyer_id]:
            purchases[buyer_id][item] += quantity
        else:
            purchases[buyer_id][item] = quantity
    else:
        purchases[buyer_id] = {item: quantity}

for buyer_id, items in purchases.items():
    print(f"Buyer {buyer_id}:")
    for item, quantity in items.items():
        print(f"{item}: {quantity}")
