from curses import ALL_MOUSE_EVENTS
from mimetypes import init
from typing_extensions import Self


class Account:
    # accountname = "Tut"
    # accountnumber = 1234
    # accountpassword = "nyawera"
    # accountamount = 5000
 def __init__(self,account_number,account_name):
    self.account_number = account_number
    self.account_name = account_name


    def deposit(self,amount):
        self.amount = amount
        self.balance+=amount
        return self.balance
        return f"your deposit is {amount} in account{self.account_number}. The balance is{self.balance}"

def withdraw(self,withdraw):
    self.amount =amount
    self.withdraw-=amount
    return self.amount
    return f"your withdraw is {amount} in account{self.account_number}. The balance is{self.balance}"


    
    # def__init__(self, account_number,account_name):
        #   self.account