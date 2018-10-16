class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """ This is generates checking account objects """
    type = "checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee


#============  part2
        #checking = Checking("balance.txt",1)
        #checking.deposit(23)
        #checking.transfer(20)
        #print(checking.balance)
        #checking.commit()
        #print(checking.balance)
#===== part 3
jack_checking = Checking("jack.txt",1)
jack_checking.transfer(20)
print(jack_checking.balance)
jack_checking.commit()
print(jack_checking.type)
print(jack_checking.__doc__)

john_checking = Checking("john.txt",1)
john_checking.transfer(20)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)
#================ part 1
#account=Account("balance.txt")
#print(account)
#print(account.balance)
#account.withdraw(10)
#print(account.balance)
#account.commit()
