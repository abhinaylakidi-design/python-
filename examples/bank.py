# Simple Bank Application

user=input("Enter the user id: ")
password=input("Enter the password: ")
Bal=int(input ("Enter your first deposite"))
username=input("Enter the user name")
epassward=input("enter your password")
if user==username and password==epassward :
    while True:
     print("1.Withdraw")
     print("2.Deposite")
     print("3.Check Bal")
     print("4.logout")
     opction=int(input("select one opction"))
     if opction==1:
         wd=int(input("Enter the withdrawel amount "))
         if wd<Bal:
             Bal=Bal-wd
             print("Collect your cash")
             print("Your current bal is ",Bal)
         else:
             print("Insufficient bal")
     if opction==2:
         dp=int(input("Enter the deposite amount "))
         Bal=Bal+dp
         print("Your current bal is ",Bal)   
     if opction==3:
         print("Your current bal is ",Bal)
     if opction==4:
         print("Thank you for using our services")
         break
else:
    print("Invalid user id or password")



