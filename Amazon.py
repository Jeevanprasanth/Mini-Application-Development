import os
print("\tAMAZON")
products=[{'product':'python book','price in Rupees':2500,'Discount in %':10,'Dicount price in Rupees':2250,'Discription':'The book written by Jeevan in 2021\nEdition => 2022','Location':'Chennai'},
        {'product':'Appel Airpods','price in Rupees':5000,'Discount in %':15,'Dicount price in Rupees':4250,'Discription':'It has nice outlook and attracting structure','Location':'Delhi'},
        {'product':'Iphone 13','price in Rupees':50000,'Discount in %':8,'Dicount price in Rupees':46000,'Discription':'The mobile phone is widely used for photos to show you!','Location':'Bangalore'},
        {'product':'Acer laptop','price in Rupees':250000,'Discount in %':19,'Dicount price in Rupees':202500,'Discription':'It is the nice gameing laptop with 4GB Graphic cards,8GB RAM and 2TB memory','Location':'Mumbai'},
        {'product':'Ball point pen','price in Rupees':10,'Discount in %':0,'Dicount price in Rupees':10,'Discription':'It write so smoothly ','Location':'Coimbatore'}]
admin=[{'user':'Jeevan','password':1234},
       {'user':'Hari@37','password':1234},
       {'user':'ohm$CDC','password':1234}]
vendor=[{'user':'Jeevan@01','password':1234,'status':'Approved'},
        {'user':'Jeevan','password':1234,'status':'Approved'},
        {'user':'Jeevan@02','password':1234,'status':'Approved'}]
buyers=[{'mail':'jeevan@gmail.com','phone':1234567890,'password':1234,'Balance':500},
        {'mail':'prasanth20@gmail.com','phone':1234567890,'password':1234,'Balance':1000},
        {'mail':'ohm@kpriet.ac.in','phone':1234567890,'password':1234,'Balance':750}]
def buyproducts():
    for s in products:
        print("\n\nproduct:",s['product'],"\nCost:",s['price in Rupees'],"\nDiscount in %:",s['Discount in %'],"\nOffer amount:",s['Dicount price in Rupees'],"\nDiscription:",s['Discription'])
def checkbalance(b):
    if b['Balance']>=sum(amount):
        print("Order has been placed Succesfully")
    else:
        print("Order coudn't be placed due to insuffient balance")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
def bill(epn):
    os.system('cls')
    print("\tAMAZON")
    while True:
            for x in products:
                if x['product']==epn:
                    xy=x['Location']
                    amount.append(x['price in Rupees'])
                    Location.append(x['Location'])
                    os.system('cls')
                    print("\n*************************************************")
                    print("\tAMAZON","                                 ")
                    print("\tName of the product==>",epn,"       ")
                    print("\tCost==>",x['price in Rupees'],"                          ")
                    print("\tLocation==>",x['Location'],"to Coimbatore","     ")
                    print("\t\tThanks for Purchasing","                ")
                    print("***************************************************")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    return 0
            else:
                print("No products are purchsed yet")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
def buy(buychoice,b):
    if buychoice==1:
        os.system('cls')
        print("\tAMAZON")
        epn=input("Enter product name for buying: ")
        for x in products:

            if x['product']==epn:
                os.system('cls')
                print("\tAMAZON")
                xy=x['Location']
                amount.append(x['price in Rupees'])
                Location.append(x['Location'])
                print("Cost:",x['price in Rupees'])
                print("Location:",x['Location'])
                checkbalance(b)
            
        for xy in south:
            if x['Location'] in south:
                print("Your order will be dispatched within 7 days")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
            elif x['Location'] not in south:
                print("Your order will be dispatched within 10 days")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
            elif x['Location']=='Coimbatore':
                print("Your order will be dispatched within 2 days")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break 
        else:
            print("Enter Valid Location for Dispatch")
            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                
    elif buychoice==2:
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
    else:
        os.system('cls')
        print("\tAMAZON")
        print("Invliad option")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
    return epn    
def addamount(b):
    b['Balance']=b['Balance']+aamount
    print("Your",aamount,"has been added Succesfully")
    input("--->>>PRESS ENTER TO CONTINUE<<<---")
add=[]
r=[]
bl=[]
amount=[]
Location=[]
south=['Andaman and Nicobar','Andhra Pradesh','Karnataka','Kerala','Lakshadweep','Puducherry','Tamil Nadu','Telangana']
while True:
    os.system('cls')
    print("\tAMAZON")
    choice=int(input("1.Admin\n2.Vendor\n3.Buyer\n4.Exit\nEnter your Choice: "))
    if choice==1:
        os.system('cls')
        print("\tAMAZON")
        user=input("Enter user name: ")
        password=int(input("Enter your password: "))
        a=None
        for i in admin:
            if user==i['user'] and password==i['password']:
                a=i
                print("\t---->>>>WELCOME TO ADMIN PAGE<<<<----")
                break
        else:
            os.system('cls')
            print("\t!!!INVALD USER NAME OR PASSWORD!!!")
            input("--->>>PRESS ENTER TO CONTINUE<<<---")
            break
        while True:
            os.system('cls')
            print("\t---->>>>WELCOME TO ADMIN PAGE<<<<----")
            ach=int(input("1.ADD or REMOVE\n2.APPROVE\n3.EXIT\nEnter your Choice: "))
            if ach==2:
                os.system('cls')
                print("\tAMAZON")
                for a in vendor:
                    
                        if a['status']=='pending':
                            print("Vendor",a['user'],"Requested for Approval")
                            apchoice=(int(input("1.Approve\n2.Reject\nEnter your choice: ")))
                            
                            if apchoice==1:
                                a['status']="Approved"
                                print("Vendor",a['user'],"has beed approved succesfully")
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                break
                            elif apchoice==2:
                                a['status']="Reject"
                                print("Vendor",a['user'],"has beed Rejected succesfully")
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                break
                else:
                    print("No New Vendor was not found for Approval")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    break                                                 
            elif ach==1:
                os.system('cls')
                print("\tAMAZON")
                achoice=int(input("1.Add\n2.Remove\n3.Exit\nEnter your choice: "))
                if achoice==3:
                    break
                elif achoice==1:
                    os.system('cls')
                    print("\tAMAZON")
                    auser=input("Creat your user I'd: ")
                    apassword=int(input("Creat your new password: "))
                    aap={'user':auser,'password':apassword}
                    vendor.append(aap)
                    print("Vendor has been added succesfully")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif achoice==2:
                    os.system('cls')
                    print('\tAMAZON')
                    vinput=input("Enter the Vendor name to remove: ")
                    for j in range(len(vendor)):
                        
                        if vendor[j]['user']==vinput:
                            del vendor[j]
                            print("Vendor has been Romoved Succesfully")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print("Due to some error Vendor coundn't be Removed")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                else:
                    print("Enter Valid Input")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==3:
                break
            else:
                os.system('cls')
                print("\t!!!INVALD USER NAME OR PASSWORD!!!")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break      
    elif choice==2:
        while True:

            os.system('cls')
            print("\tAMAZON")
            select=int(input("1.New User\n2.Existing user\n3.Exit\nEnter your Choice: "))
            if select==3:
                break #Need to be checked(Programming cracing : break is not working properly)
            elif select==1:
                os.system('cls')
                print("\tAMAZON")
                nuser=input("Creat your user I'd: ")
                npassword=int(input("Creat your new password: "))
                uap={'user':nuser,'password':npassword,'status':'pending'}
                vendor.append(uap)
                print("Request has been Send ")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif select ==2:
                os.system('cls')
                print("\tAMAZON")
                vuser=input("Enter user name: ")
                vpassword=int(input("Enter your password: "))
                v=0
                for j in vendor:
                    if vuser==j['user'] and vpassword==j['password'] :
                        if j['status']=='Approved':
                            v=j
                            break
                        else:
                            print("Your Request has been waitng for approval ")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                else:
                    print("Invalid User name or Password")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")

                if v==0:
                    continue
                while True:
                    os.system('cls')                
                    print("---->>>>Welcome ",v['user'],"<<<<----")
                    pchoice=int(input("1.Add Product\n2.Remove Product\n3.Exit\nEnter your choice: "))
                    if pchoice==1:
                        os.system('cls')
                        print("\tAMAZON")
                        print("\t\tADD PRODUCTS")
                        nproduct=input("Enter Product Name: ")
                        nprice=int(input("Enter price in Rupees of the product: "))
                        ndiscount=int(input("Enter Discount in percentage for the product: "))
                        ndisprice=int(input("Enter Discount price: "))
                        ndis=input("Enter product discription: ")
                        loc=input("Enter the Location: ")
                        pap={'product':nproduct,'price in Rupees':nprice,'Discount in %':ndiscount,'Dicount price in Rupees':ndisprice,'Discription':ndis,'Location':loc}
                        products.append(pap)
                        print("Product has been Added  Succesfully")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")  
                    elif pchoice==2:
                        os.system('cls')
                        print('\tAMAZON')
                        rinput=input("Enter the product to remove: ")
                        for i in range(len(products)):
                            
                            if products[i]['product']==rinput:
                                del products[i]
                                print("Product has been Romoved Succesfully")
                                print(products)
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                break
                        else:
                            print("Product doest not have")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    elif pchoice==3:
                        break
                    else:
                        os.system('cls')
                        print("\tAMAZON")
                        print("Invalid product option")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")               
            else:
                print("Account coudn't be created due to some issues")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                continue  
    elif choice==3:
        while True:
            os.system('cls')
            print("\tAMAZON")
            bchoice=int(input("1.New User\n2.Existing user\n3.Exit\nEnter your Choice: "))
            if bchoice==3:
                break
            elif bchoice==2:
                os.system('cls')
                print("\tAMAZON")
                buser=input("Enter valid mail i'd: ")
                bph=int(input("Enter vlaid phone number: "))
                bpassword=int(input("Enter your password: "))
                while True:
                    b=None
                    for k in buyers:
                        if buser==k['mail'] and bph==k['phone'] and bpassword==k['password']:
                            b=k
                            os.system('cls')
                            print("Account loggedin succesfully")
                            bpchoice=int(input("1.Buy Products\n2.View Balance\n3.Add to Card\n4.Add Amount\n5.Generate Bill\n6.Exit\nEnter your Choice: "))
                            break
                    else:
                        os.system('cls')
                        print("Account doesn't exisit")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        break
                    if bpchoice==6:
                        break
                    elif bpchoice==1:
                        os.system('cls')
                        print("\tAMAZON")
                        buyproducts()
                        cproduct=input("Choose your product to buy: ")
                        add.append(cproduct)
                        print("Products are added to card Succesfully")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    elif bpchoice==2:
                        print("Your Amazon Balance is",b['Balance'])
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    elif bpchoice==4:
                        aamount=int(input("Enter the amount to add: "))
                        addamount(b)
                    elif bpchoice==5:
                        bill(epn)
                    elif bpchoice==3:
                        os.system('cls')
                        print("\tAMAZON")
                        cardchoice=int(input("1.View to Card\n2.Remove from Card\n3.History\n4.Exit\nEnter your choice: "))
                        if cardchoice==1:
                            os.system('cls')
                            print("\tAMAZON")
                            str1=" "
                            os.system('cls')
                            print("The Product Succesfully saved in card:",str1.join(add))
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            buychoice=int(input("1.Buy\n2.Exit\nEnter your choice: "))
                            epn = buy(buychoice,b)
                            bill(epn)
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            if buychoice==4:
                                break
                            else:
                                print("Enter valid option")
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        elif cardchoice==4:
                            break
                        elif cardchoice==2:
                            os.system('cls')
                            print("\tAMAZON")
                            reproduct=input("Enter the product to remove from your Card: ")
                            r.append(reproduct)
                            add.remove(reproduct)
                            print("Product has been Removed from card Succesfully")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        elif cardchoice==3:
                            os.system('cls')
                            print("\tAMAZON")
                            huchoice=input("Enter the valid user name to access history: ")
                            hpchoice=int(input("Enter the password to access history: "))
                            if huchoice=="kpriet" and hpchoice==123:
                                os.system('cls')
                                print("\tAMAZON")
                                print("\t---->>>>HISTORY<<<<----")
                                str1=" "
                                print("products that add by you in histroy ==>",str1.join(add))
                                str2=" "
                                print("Products that remove by you in histroy ==>",str2.join(r))
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            else:
                                os.system('cls')
                                print("\tAMAZON")
                                print("OOPS WRONG USER NAME OR PSSWORD")
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        else:
                            os.system('cls')
                            print("\tAMAZON")
                            print(">>ERROR 404!<<")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    else:
                            os.system('cls')
                            print("Enter valid option")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
               
                    
            elif bchoice==1:
                os.system('cls')
                print("\tAMAZON")
                buser=input("Creat your email I'd: ")
                bph=int(input("Enter your phone number: "))
                bpassword=int(input("Creat your new password: "))
                bap={'mail':buser,'phone':bph,'password':bpassword,'Balance':0}
                buyers.append(bap)
                print("Account has been created Succesfully")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")  
    elif choice==4:
        exit()
    else:
        os.system('cls')
        print("---->>>INVALID CHOICE CHOOSE 1 TO 3 OPTION<<<---")
        input("      --->>>PRESS ENTER TO CONTINUE<<<---")
        break
