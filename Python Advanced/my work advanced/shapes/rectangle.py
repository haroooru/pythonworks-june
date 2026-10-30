l = [12,13,14,15,16]
new = []

for i in l:
    if i <


        class Account:
            def __init__(self):
                self.Accnumber = input("Enter Account Number: ")
                self.Acctname = input("Enter Account Name: ")
                self.balance = int(input("Enter Balance: "))

            def withdraw(self):
                amount = int(input("Enter amount to withdraw: "))
                if amount <= self.balance:
                    self.balance = self.balance - amount
                    print("Withdraw successful")
                else:
                    print("Withdraw failed")

            def deposit(self):
                amount = int(input("Enter amount to deposit: "))
                self.balance = self.balance + amount
                print("Deposit successful")

            def showbalance(self):
                print("Current balance:", self.balance)


        # create two account objects
        a1 = Account()
        a2 = Account()

        # store them in a list
        l = [a1, a2]

        # print details of both accounts
        for k in l:
            print(f"Account no: {k.Accnumber} Name: {k.Acctname} Balance: {k.balance}")
