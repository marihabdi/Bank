
class Fund:
    def __init__(self, fund_kind):
        self.__fund_name = {0: "Money Market", 
                            1: "Prime Money Market",
                            2: "Long-Term Bond",
                            3: "Short-Term Bond",
                            4: "500 Index Fund",
                            5: "Capitol Value Fund",
                            6: "Growth Equity Fund",
                            7: "Growth Index Fund",
                            8: "Value Fund",
                            9: "Value Stock Index"
                            }
        self.fund_kind = fund_kind
        self.amount = 0
        self.transaction = []
    def deposit(self, amount, steps, passed):
        if passed:
            self.amount += amount
        self.add_data(steps, passed )
        
    def withdraw(self, amount, steps ):
       
        if amount > self.amount:
                passed = False
        else:
            self.amount -= amount
            passed = True
        self.add_data(steps, passed)
        return passed
    
    def add_data(self,steps, passed):
        status = "" if passed else " (Failed)"
        self.transaction.append(f"{steps} {status}")
    def name(self):
        return self.__fund_name[self.fund_kind]
    def __str__(self):
        result = f'{self.__fund_name[self.fund_kind]}: ${self.amount}\n'
        for t in self.transaction:
            result += f" {t}\n"
        return result