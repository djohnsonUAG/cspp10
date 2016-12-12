bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while(" "):
    if choice == "1": 
        amount = input("How much to withdraw: ")
        bank_acount = bank_acount - int(amount) 
    elif choice == "2": 
        amount = input("How much to deposit: ")
        bank_account = bank_account + int(amount) 
    elif choice == "3": 
        

        print("1. Withdraw \n2. Deposit \n3. Exit")
        break
    choice = input("Pick from above [1|2|3]:")                                                                                                                           