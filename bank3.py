l = []
net_amount = 0
while True:
    transaction = input("Enter Transaction: ")
    if transaction == "Exit".casefold():
        break
    else:
        transaction = transaction.split(" ")
        if transaction[0] == "D".casefold():
            net_amount = net_amount + int(transaction[1])
        elif transaction[0] == "W".casefold():
            net_amount = net_amount - int(transaction[1])
        l.append(transaction)
print(l)
if net_amount <= 0:
    print("Withdrawal is not allowed! Your current balance is less by {}"
          " than your withdrawal amount.".format(-1 * net_amount))
else:
    print(net_amount)