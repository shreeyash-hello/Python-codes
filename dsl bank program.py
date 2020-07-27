def bank():
    while True:
        checking_balance = 500
        savings_balance = 2000
        newCheck = 500 + 0

        choice = input("""Choose one of the choices below.
    d(deposit) p(print current balance) w(withdraw)
    t(transfer) q(quit): """)
        if (choice == 'q' or choice == 'Q'):
            break  # exit loop
            end

        if (choice == 'd' or choice == 'D'):
            deposit = float(input("Put amount: "))
            newCheck = checking_balance + deposit
            checking_balance = newCheck
        # print("New checking balance is $%.2f"%newCheck)

        if (choice == 'p' or choice == 'P'):
            print("New checking balance is $%.2f" % newCheck)

        if (choice == 'w' or choice == 'W'):
            withdraw = float(input("Put amount: "))
            newCheck = checking_balance - withdraw
            checking_balance = newCheck