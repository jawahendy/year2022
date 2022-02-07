def bonAppetit(bill, k, b):
    n = len(bill)
    ItemsAna = [bill[i] for i in range(n) if i != k]

    BillAna = sum(ItemsAna)//2

    if BillAna == b:
        print('Bon Appetit')
    else:
        print(str(b - BillAna))