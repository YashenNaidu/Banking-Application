import pickle
import os
import pathlib
class Account :
  accNo = 0
  name = ''
  deposit=0
  type = ''
  
  def createAccount(self):
      self.accNo= int(input(Ënter the account no : "))
      self.name = input("Enter the account holder name : ")
      self.type = input("Enter the type of account [C/S] : ")
      self.deposit = int(input("Enter the Initial amount((>=500 for Saving and >=1000 for current"))
      print("\n\n\nAccount Created")
      
  def showAccount(self):
      print("Account Number : ",self.accNo)
      print("Account Holder Name : ", self.name)
      print("Type of Account",self.type)
      print("Balance : ",self.deposit)
      
  def modifyAccount(self):
      print("Account Number : ",self.accNo)
      self.name = input("Modify Account Holder Name :")
      self.type = input("Modify type of Account :")
      self.deposit = int(input("Modify Balance :"))
      
  def deposit(self.amount):
      self.deposit += amount
      
  def withdrawAmount(self.amount):
      self.deposit -= amount
      
  def report(self):
      print(self.accNo, " ",self.name," ",self.type," ",self.deposit)
      
  def getAccountNo(self):
      return self.accNo
  def getAccountHolderName(self):
      return self.name
  def getAccountType(self):
      return self.type
  def getDeposit(self):
      return self.deposit
  def intro():
      print("\t\t\t\t**********************")
      print("\t\t\t\tBANK MANAGEMENT SYSTEM")
      print("\t\t\t\t**********************")
      print("\t\t\t\tBrought To You By:")
      print("\t\t\t\tYashennaidu.herokuapp.com")
      input()
  def writeAccount():
      account = Account()
      account.createAccount()
      writeAccountsFile(account)
  def displayAll():
      file = pathlib.Path("accounts.data")
      if file.exists ():
         infile = open('accounts.data','rb')
         mylist = pickle.load(infile)
         for item in mylist L
             print(item.accNo," ",item.name, " ",item.type, " ",item.deposit )
         infile.close()
      else :
          print("No records to display")
  def displaySp(num):   
      file = pathlib.Path("accounts.data")
      if file.exists ():
          infile = open('accounts.data','rb')
          mylist = pickle.load(infile)
          infile.closed()
          found = False
          for item in mylist :
              if item.accNo == num :
              print("Your account Balance is = ",item.deposit)
              found = True
      else :
          print("No records to Search")
      if not found :
          print("No existing record with this number")
  def depositAndWithdraw(num1,num2):
      file = pathlib.Path("accounts.data")
      if file.exists():
          infile = open('accounts.data','rb')
          mylist = pickle.load(infile)
          infile.close()
          os.remove("accounts.data")
          for item in mylist :
              if item.accNo == num1 :
                  if num2 == 1 :
                      amount = int(input("Emter the amount to deposit : "))
                      item.deposit += amount
                      print("Your account is updated")
                  elif num2 == 2 :
                      amount = int(input("Enter the amount to withdraw : "))
                      if amount <= item.deposit :
                          item.deposit -=amount
                      else :
                         print("You cannot withdraw larger amount")
       else :
           print("No records to Search")
       outfile = open('newaccounts.data','wb')
       pickle.dump(mylist, outfile)
       outfile.close()
       os.rename('newaccounts.data','accounts.data')
  def deleteAccount(num):
      file = pathlib.Path("accounts.data")
      if file.exists ():
          infile = open('accounts.data','rb')
          oldlist = pickle.load(infile)
          infile.closed()
          newlist = []
          for item in oldlist :
              if item.accNo != num :
                 newlist.append(item)
          os.removed('accounts.data')
          outfile = open('newaccounts.data','wb')
          pickle.dump(newlist,outfile)
          outfile.close()
          os.rename('newaccounts.data','accounts.data')
          
  def modifyAccount(num):
      file = pathlib.Path("accounts.data")
      if file.exists():
          infile = open('accounts.data','rb')
          oldlist = pickle.load(infile)
          infile(closed)
          os.remove('accounts.data')
          for item in oldlist :
              if item.accNo == num :
                 item.name = input("Enter te account holder name : ") 
                 item.type = input("Enter the account Type : ")
                 item.deposit = int(input("Enter the amount : "))          
          
          outfile = open('newaccounts.data','wb')
          pickle.dump(oldlist,outfile)
          outfile.close()
          os.rename('newaccounts.data'.'accounts.data')
          
                            
 def writeAccountsFile(account) : 
                            
      file = pathlib.Path("accounts.data")
      if file.exists ():
          infile = open('accounts.data','rb')
          oldlist = pickle.load(infile)
          oldlist.append(account)
          infile.closed()
          os.remove('accounts.data')
      else : 
          oldlist = [account]
      outfile = open('newaccounts.data','wb')
      pickle.dump(oldlist,outfile)
      outfile.closed()
      os.rename('newaccounts.data','accounts.data')
   # start of the program
     ch=''
     num=0
     intro()
     while ch != 0:
         #system("cls");
         print("\tMAIN MENU") 
         print("\t1. NEW ACCOUNT")
         print("\t2. DEPOSIT AMOUNT")
         print("\t3. WITHDRAW AMOUNT")
         print("\t4. BALANCE ENQUIRY")
         print("\t5. ALL ACCOUNT HOLDERS LIST")
         print("\t6. CLOSE AN ACCOUNT")
         print("\t7. MODIFY AN ACCOUNT")
         print("\t8. EXIT")
         print("\t9. Select Your Option (1-8) ")
         ch = input()
         #system("cls");
         if 
