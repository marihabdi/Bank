from Fund import *


class Account:
    def __init__(self, client_id, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.client_id = client_id
        self.funds = []
        for i in range(10):
            self.funds.append(Fund(i))

    def deposit(self, fund_id, amount, steps, passed):
        if fund_id > 9 or fund_id < 0:
            return f"ERROR: Deposit for a non-existent fund"
        else:
            self.funds[fund_id].deposit(amount, steps, passed)
           

    def withdraw(self, fund_id, amount, steps):
        
        if fund_id > 9 or fund_id < 0:
            return f"Error: Withdraw for a non-existent fund"
       
        if fund_id == 2:
             
            if self.funds[2].amount < amount:
                if self.funds[2].amount + self.funds[3].amount > amount:
                    temp_amount = self.funds[2].amount
                    step1 = f'{steps.split(" ")[0]} {steps.split(" ")[1]} {str(temp_amount)}'
                    step2 = f'{steps.split(" ")[0]} {steps.split(" ")[1]} {amount - temp_amount}'
                    
                    self.funds[2].withdraw(self.funds[2].amount, step1)
                    self.funds[3].withdraw(amount - temp_amount, step2)
                
                    
                else:
                    return f"Error: Not enough funds to withdraw {amount} from {self.firstname} {self.lastname} {self.funds[fund_id].name()}"

        elif not self.funds[fund_id].withdraw(amount, steps):
            return f"Error: Not enough funds to withdraw {amount} from {self.firstname} {self.lastname} {self.funds[fund_id].name()}"

    def __lt__(self, x):
        key = x
        if x is Account:
            key = x.client_id
        if self.client_id < key:
            return True
        else:
            return False

    def __le__(self, x):
        key = x
        if self.client_id <= key:
            return True
        else:
            return False

    def __eq__(self, x):
        key = x
        if x is Account:
            key = x.client_id
        if self.client_id == key:
            return True
        else:
            return False

    def __ne__(self, x):
        key = x
        if x is Account:
            key = x.client_id
        if self.client_id != key:
            return True
        else:
            return False

    def __ge__(self, x):
        key = x
        if x is Account:
            key = x.client_id
        if self.client_id >= key:
            return True
        else:
            return False

    def __gt__(self, x):
        key = x
        if x is Account:
            key = x.client_id
        if self.client_id > key:
            return True
        else:
            return False

    def __str__(self):
        result = f"{self.firstname} {self.lastname} Account ID: {self.client_id}\n"
        for each in self.funds:
            result += f"{each.name()}: ${each.amount}\n"
        return result




