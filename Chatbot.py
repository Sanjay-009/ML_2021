# Banking service chatbot
# This chatbot is used to customer service for Banking  
"""
    This chatbot works with following sequence
    1.The bot starts with greeting and introduce itself.
    2.The bot will asks for the name and wish the person.
    3.The bot offers some options related to the customer queries,bank offers and related information.
    4.Based upon the input given by the user it will respond to them
"""
import random
def Intro():
    wish_list=["Hi! Iam Bankbot.I am here to help you,Can I know your name please?",
    "Hello ,Nice to see you.I am Bankbot to help you.Tell me your name please!",
    "Hi There!,It is good to talk with you,May I know your name please?"
    ]
    print(random.choice(wish_list))
def Bot_features(name):
    print("Hello,",name,'!!!')
    print('------------------------------------------------------------------------------------')
    print("Press 1 to check your account details")
    print("press 2 to transfer the amount to another account")
    print("press 3 to deposit the amount to your account")
    print("press 4 to check loans offered by the bank")
    print("press 5 to exit this chat")
    print('------------------------------------------------------------------------------------')
def details(name,amount):
    ac_num=input("Enter your account number : ")
    password=input("Enter your password : ")
    print('--------------------------------')
    print("Customer Name :",name)
    print("Account no : ",ac_num)
    print('Branch code : 106789')
    print('IFSC : SBIN00127368')
    print("Balance amount : ",amount)
    print('Phone : 9367239193')
    print('State Bank Of India,Tirupathi,Andhra pradesh,517619')
    print('---------------------------------')
def transaction(name,amount):
    ac_num=input("Enter your account number : ")
    password=input("Enter your password : ")
    Transfering_account=input("Enter the account number in which you want to transfer : ")
    Transfering_amount=input("Enter the amount to be transfered : ")
    if(amount>=int(Transfering_amount)):
        amount=amount-int(Transfering_amount)
        print(f"Hi {name} your a/c no : {ac_num} is debited with Rs.{Transfering_amount} and remaining balace in your account is Rs.{amount}")
    else:
        print("Your account has no sufficient balance to transact..")
    print('---------------------------------')
def deposition(name,amount):
    ac_num=input("Enter your account number : ")
    deposit_amount=input("Enter the amount to be deposite : ")
    amount=amount+int(deposit_amount)
    print(f"Hi {name} your a/c no : {ac_num} is credited with Rs.{deposit_amount} and remaining balace in your account is Rs.{amount}")
    print('---------------------------------')
def loan_offers():
    loans=["Home loan with interest 9.2% p/a","Crop loan for farmers with interest 6% p/a","Gold loan with Interest 8% p/a","Land loan with 8.6% p/a"]
    for i in loans:
        print(i)
    print('---------------------------------')
def Bot_work():
    Intro()
    name=input("Please enter your name : ")
    print()
    Bot_features(name)
    num=int(input("Enter the number : "))
    while(num!=5):
        Amounts=[25000,32560,10000,5000,2500,3000]
        amount=random.choice(Amounts)
        if(num==1):
            details(name,amount)
        elif(num==2):
            transaction(name,amount)
        elif(num==3):
            deposition(name,amount)
        elif(num==4):
            loan_offers()
        else:
            print("Please enter valid number....")
            print('---------------------------------')
        num=int(input("Enter the number :", ))
    if(num==5):
            print("Thank you,Have a nice day!")
            print('---------------------------------')

Bot_work()