import os
import re
import time
userno=102
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
users=[{'name':'Jeevan Prasanth','mail':'jeevan@gmail.com','password':1234,'userid':100},
       {'name':'Krishna','mail':'hari@gmail.com','password':1234,'userid':101},
       {'name':'Ohm Prakash','mail':'ohm@gmail.com','password':1234,'userid':102}]
while True:
       os.system('cls')
       print("\tSPLITWISE")
       select=int(input("1.New user\n2.Existing user\n3.Exit\nEnter your choice: "))
       if select==3:
              break
       elif select==1:
              os.system('cls')
              print("\tSPLITWISE")
              uname=input("Enter your name: ")
              umail=input("Enter your email id: ")
              if(re.search(regex,umail)):   
                     print("Valid Email")  
              else:   
                     print("Invalid Email")  
                     break
              upass=int(input("Enter your password: "))
              userno+=1
              ua={'name':uname,'mail':umail,'password':upass,'userid':userno}
              users.append(ua)
              print(uname,"has succesfully registed as new user in SPLITWISE","\nuser id: ",userno)
              input("--->>>PRESS ENTER TO CONTINUE<<<---")
       elif select==2:
              os.system('cls')
              print("\tSPLITWISE")
              email=input("Enter mail I'D: ")
              if(re.search(regex,email)):   
                     print("Valid Email")  
              else:   
                     print("Invalid Email")  
                     break
              epass=int(input("Enter password: "))
              for b in users:
                     if b['mail']==email and b['password']==epass:
                           os.system('cls')
                           print("Welcome",b['name']) 
                           cgrp=int(input("1.Creat New Group\n2.Join Group\n3.Exit\nEnter your choice: "))
                           if cgrp==3:
                                  input("--->>>PRESS ENTER TO CONTINUE<<<---")
                           elif cgrp==1:
                                  os.system('cls')
                                  grpname=input("Group Name: ")
                                  print("Loading...")
                                  time.sleep(3)
                                  os.system('cls')
                                  grptype=int(input("1.Travel\n2.Home\nEnter your choice: "))
                                  if grptype==1:
                                         time.sleep(3)
                                         os.system('cls')
                                         print(grpname,"has succesfully created")
                                         input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                         os.system('cls')
                                         print("\t",grpname,"\n\tTravel")
                                         travelamember=input("Enter Name to add people: ")
                                         if b['name']==travelamember:
                                                 print(travelamember,"has succesfully added to",grpname)
                                                 input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                                 break
                                         else:
                                          print(travelamember,"is not a user of SPLITWISE")
                                          input("--->>>PRESS ENTER TO CONTINUE<<<---")
              else:
                     os.system('cls')
                     print("Account dosent exist")
                     input("--->>>PRESS ENTER TO CONTINUE<<<---")
       else:
              os.system('cls')
              print("Invalid input from user selection page")
              input("--->>>PRESS ENTER TO CONTINUE<<<---")
       