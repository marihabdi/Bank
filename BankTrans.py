#Mariama Abdi
#6/3/2022
#CSS 340
#Instructor Dimpsey, Robert

from Node import *
from Account import *


class BankTrans:
    def __init__(self):
        self.__accounts = Node()
    def open_account(self,client_id,last_name, first_name):
        client_id = int(client_id)
        if self.__exists(client_id):
            return f"ERROR: Account {client_id} is already open. Transaction refused.\n"
        self.__accounts.insert(Account(client_id, last_name, first_name))
    def deposit(self, client_id, fund_id, amount):
        return self.__deposit(client_id, fund_id, amount, f"D {client_id}{fund_id} {amount}", True)
    def __deposit(self, client_id, fund_id, amount, steps, succes):
        client_id = int(client_id)
        fund_id = int(fund_id)
        amount = int(amount)
        account = self.__accounts.search(client_id)
        if account is not None:
            return account.deposit(fund_id, amount, steps, succes)
        else:
            return f"ERROR: Account {client_id} not found. Deposit refused.\n"
    def withdraw(self, client_id, fund_id, amount):
        client_id = int(client_id)
        fund_id = int(fund_id)
        amount = int(amount)
        account = self.__accounts.search(client_id)
        if account is not None:
            return account.withdraw(fund_id, amount, f"W {client_id}{fund_id} {amount}")
        else:
            return f"ERROR: Account {client_id} not. Withdraw refused."
    def transfer(self,src,dst,amount):
        input_client_id = int(src[0:4])
        input_fund_id = int(src[4])
        to_client_id = int(dst[0:4])
        to_fund_id = int(dst[4])
        input_account = self.__accounts.search(input_client_id)
        if input_account is None:
            return f"ERROR: Account {input_client_id} not found. Transferal refused.\n"
        to_account = self.__accounts.search(to_client_id)
        if to_account is None:
            return f"ERROR: Account {to_client_id} not found. Tansferal refused."
        source_resp = input_account.withdraw( input_fund_id, int(amount) , f"T {src} {amount} {dst}")
        if source_resp is not None:
            passed = False
        else:
            passed = True
            to_resp = self.__deposit(to_client_id, to_fund_id, amount, f"T {src} {amount} {dst}", passed)
            if source_resp is not None and to_resp is not None:
                return f"{source_resp}\n{to_resp}"
            elif source_resp is not None:
                return f"{source_resp}"
            elif to_resp is not None:
                return f"{to_resp}"
    def __exists(self, client_id):
        client_id = int(client_id)
        if self.__accounts.search(client_id) is not None:
            return True
        else:
            return False
    def history(self, client_id, fund_ids):
        account: Account = self.__accounts.search(client_id)
        if account is not None:
            if len(fund_ids) == 1:
                fund_id = int(fund_ids[0])
                result = f"Transaction History for {account.firstname} {account.lastname}"
                result += f"{account.funds[fund_id]}\n"  
                
            else:
                result = f"Transaction History for {account.firstname} {account.lastname} by fund.\n"
                for i in range(10):
                    if account.funds[i].amount >= 0:
                        result += f"{account.funds[i]}" 
                        
            return result
        else:
            return f"ERROR: Account {client_id} not found. Transaction refused.\n"
    def report_all(self):
        return   self.__accounts.nodes()
        
    
def main():
    bank = BankTrans()
    
    fin = open("BankTransIn.txt", "r")
    fout = open("My_BankTransOut.txt", "w")
    for i in fin.readlines():
        data = i.rstrip("\n").split()
        trans_type = data[0]
        if trans_type == 'O':
            last_name = data[1]
            first_name = data[2]
            client_id = data[3]
            response = bank.open_account(client_id, last_name, first_name)
            if response is not None:
                fout.write(response + "\n")
                print(response + "\n")
        elif trans_type == 'D':
            client_id = data[1][0:4]
            fund_id = data[1][4]
            amount = data[2]
            response = bank.deposit(client_id, fund_id, amount)
            if response is not None:
                fout.write(response + "\n")
                print(response)

        elif trans_type == 'W':
            client_id = data[1][0:4]
            fund_id = data[1][4]
            amount = data[2]
            
            response = bank.withdraw(client_id, fund_id, amount)


            if response is not None:
                fout.write(response + "\n")
                print(response)
        elif trans_type == 'T':
            src = data[1]
            dst = data[3]
            amount = data[2]
            response = bank.transfer(src, dst, amount)
            if response is not None:
                fout.write(response)
                print(response )
        elif trans_type == 'H':
            if len(data[1]) == 4:
                client_id = int(data[1])
                fund_ids = list(range(10))
            else:
                client_id = int(data[1][0:4])
                fund_ids = [data[1][4]]
            fout.write(bank.history(client_id,fund_ids)+"\n")
            print(bank.history(client_id,fund_ids))
             


        else:
            fout.write("Error: Invalid Transaction Type\n")
            print("Error: Invalid Transaction Type\n")
    fout.write("\n")
    print("\n")
    fout.write("Proccessing Done. Final Balances\n")
    print("Proccessing Done. Final Balances\n")
    for n in bank.report_all():
       fout.write(f"{n}\n")
       print(f"{n}")
    
    fin.close()
    fout.close
if __name__ == "__main__":
    main()








