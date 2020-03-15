#create a bank account where you can add and withdraw funds
#withdraw can't be more than the current amount in bank account
#create owner and balance

class Account():
    def __init__(self,owner,balance = 0):
        
        self.owner = owner
        self.balance = balance
        
#now we are creating a deposit function               
    def deposit(self,dep_amt):
        
        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')
        print(f"{self.owner}'s new balance is {self.balance}")

#now lets make a withdrawl function to check to see if the owner has enough money to pull from the account     
    def withdrawl(self,wd_amt):
        
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print('Withdrawl Accepted ')
            print(f"{self.owner}'s new balance is {self.balance}")
        else:
            print('Sorry not enough funds!')
            print(f"{self.owner}'s new balance is {self.balance}")
    
    def __str__(self):
        return f'Owner: {self.owner} \nBalance: {self.balance}'

#Lets now make an owner to see if our functions run as we would like 

a = Account('Sam',500)

print(a.owner)
print(a.balance)

print('---------')

#now lets make a deposit to Sam's account and see fi the deposit function we wrote works!

a.deposit(1000)
print('---------------------')

#Great! it's working as intended

#now Let's check withdrawl and remember, you can't pull out more than what you have in the account!

a.withdrawl(1500)
print('--------------------')

#now if we try to pull money out again it should tell us no

a.withdrawl(500)
print("--------------------")


print(a.balance)
