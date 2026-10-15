import calc as ca


USER_DATA = {
    "username": "admin",
     "acc.no" : 123456,
     "pin"    :  1234,
     "balance": 1000
     }

def user_info():
     
    if USER_DATA and USER_DATA["username"]:
        return f"\nhi user {USER_DATA['username']} your account no is {USER_DATA['acc.no']}"

    else:
        print("user not found")


def deposit(deposit_amount):
    if deposit1_amount:
        amount = ca.deposit_cal(USER_DATA["balance"], deposit_amount)
        USER_DATA["balance"] = amount
        return amount
    else:
        print("amount not found")



def withdraw(withdraw_amount):
    if withdraw_amount:
        amount = ca.withdraw_cal(USER_DATA["balance"], withdraw_amount)
        USER_DATA["balance"] = amount
        return amount
    else:
        print("amount not found")


def balance():
    return USER_DATA["balance"]


def main():
    print("welcome to the pawan public bank")
    pin_no = int(input("enter your pin number: "))

    if USER_DATA and USER_DATA["pin"] == pin_no:
       
       print(user_info())

    while True:

       choice = int(input("""
        1. deposit 
        2. withdraw
        3. balance
        4. exit
        Enter your choice: """))
       
       match choice:
           case 1:
               amount = int(input("enter the amount :"))
               print(f"deposite sucessfully, your balance is {deposit(amount)}")
               
           case 2:
                amount = int(input("enter the amount :"))
                print(f"withdrawn successfully, your balance is {withdraw(amount)}")

           case 3:
                print(f"your total balance is {balance()}")

           case 4:
                print("thank you for using our bank")
                break


    else:
        print("invalid pin number")


if __name__ == "__main__":
    main()