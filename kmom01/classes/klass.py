import random

class BankAccount:
    # statiskt attribut som inte är kopplad till en instans
    interest = 2.3
    
    # constructor
    # self refererar till objektet i minnet
    def __init__(self, ssn, balance, name):
        self.ssn = ssn
        self._balance = balance # med _ i attributet så gör vi det privat,
        # en skillnad mot andra språk så kan vi kalla på attributet genom att lägga till
        # _, men det visar utvecklaren att den inte ska kallas på.
        # I metoderna kallar vi attributet genom _, men det visar att den inte ska
        # kallas på utanför funktionerna
        self.id_number = random.randint(100, 1000)
        self.name = name
        self.interest = BankAccount.interest

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return True
        return False
    
    def deposit(self, amount):
        self.balance += amount
        
    
    def transfer(self, amount, to):
        if self.withdraw(amount):
            to.deposit(amount)
        
    @staticmethod
    def calc_interest(amount):
        return amount * BankAccount.interest
        

    def __add__(self, other):
        return self._balance + other._balance # summerar _balans från två instanser
    
    def __add__(self, other):
        return self._balance - other._balance # visar self._balance - other._balance
    
    def __iadd(self, other):
        return self._balance += other._balance # uppdaterar värdet
    
    # det finns specialmetoder för alla operatorer

# instans av classen BankAccount
acc1 = BankAccount("98737", 1000, "löning")
acc2 = BankAccount("98737", 600, "pension")

#print(acc1.balance)
#print(acc2.balance)
#acc1.transfer(200, acc2)
#print(acc1.balance)
#print(acc2.balance)
#print(BankAccount.calc_interest(250))

