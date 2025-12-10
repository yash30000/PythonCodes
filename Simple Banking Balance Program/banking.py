balance = 1000

while True:
    print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    ch = int(input("Choose: "))

    if ch == 1:
        print("Balance:", balance)
    elif ch == 2:
        amt = int(input("Enter amount: "))
        balance += amt
        print("Deposited!")
    elif ch == 3:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn!")
        else:
            print("Insufficient Balance")
    else:
        break
