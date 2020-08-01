class Bank_Account: 
    def __init__(self): #access the instances
        self.balance=0 #initally 0
        print("Hiii Welcome !!") #To Print Normal Statements
        print("\nWhen you Create Account, Your Details are save in text file..\nYou can see file. Just Minimise screen..")

    def open(self): #access the instances
        f=open("Data.txt","a") #open text file and data.txt is name of file
        name=input("Enter Name : ")
        cno=input("Enter Account Number : ")
        data=name+"--->"+cno+"\n" #variable to store 
        f.write(data) #writes file
        f.close() #closes a file

  
    def deposit(self): #function to deposit
        amount=float(input("Enter amount to be Deposited : ")) 
        self.balance += amount #As initially 0 so, will get ad with entered amount
        print("\n Amount Deposited:",amount) #To display Amount
        
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdraw : ")) 
        if self.balance>=amount: 
            self.balance-=amount #subtract from initial amount
            print("\n Withdraw Amount : ", amount) 
        else: 
            print("\n Not Much Balance ") #if amount less
  
    def display(self): 
        print("\nBalance Available =",self.balance) #show overall amount in account 
  
   
# object of class  Bank_Account
s = Bank_Account() 
   
# Call functions with object s
s.open()
s.deposit() 
s.withdraw() 
s.display() 
