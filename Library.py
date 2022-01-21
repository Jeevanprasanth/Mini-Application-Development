import os
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
admin=[{'mail':'jeevan@gmail.com','password':1234},
       {'mail':'hari@gmail.com','password':1234},
       {'mail':'ohm@gmail.com','password':1234}]
book=[{'sub':'python','title':'Complete Reference','Author':'Kerty Syer','Publisher':'Com tech','editon':8,'page':504,'ISBN':45622,'copies':5,'cost':500,'Library':'Anna Centenary Library'}]
students=[{'name':'Jeevan prasanth S','roll_no':'19ME044','batch':2023,'mail':"19me044@kpriet.ac.n",'ph':8098710914,'balance':2000,'penalty':0}]
take=[{'book':'python','fdate':"11/01/2002",'ddate':"25/01/2022",'penalty':0}]
r=[{'book':'python','fdate':"11/01/2002",'ddate':"25/01/2022",'penalty':0}]
add=[]
late=0
lostbook=0
lostmember=0
zz=0
def showbook():
    for j in  book:
        print("\n",j['sub'],j['copies'])  
def change(yz):
    for z in book:
        print(z['sub'])
        
        if z['sub']==yz:
            print("\n",z['sub'],z['title'],z['Author'],z['Publisher'],z['editon'],z['page'],z['ISBN'],z['copies'],z['cost'],z['Library'])
            cc=int(input("Enter to change No. of copies: "))
            a['copies']=cc
            showbook()
            input("--->>>PRESS ENTER TO CONTINUE<<<---")
        else:
            os.system('cls')
            print('\tAnna Centenary Library')
            print("Book not found") 
            input("--->>>PRESS ENTER TO CONTINUE<<<---")
def fine(lost,lostbook,lostmember):
    i['penalty']=lost+lostbook+lostmember
while True:
    os.system('cls')
    print("\tAnna Centenary Library")
    choice=int(input("1.Admin\n2.Student Login\n3.Exit\nEnter your Choice: "))
    if choice==1:
        os.system('cls')
        print("\tAnna Centenary Library")
        email=input("Enter maili'd name: ")
        if(re.search(regex,email)):   
            print("Valid Email")  
        else:   
            print("Invalid Email")  
            break
        password=int(input("Enter your password: "))
        a=None
        for i in admin:
            if email==i['mail'] and password==i['password']:
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
            ach=int(input("1.ADD New Admin\n2.Add Book\n3.Remove Book\n4.Change details of book\n5.Available books\n6.Exit\nEnter your Choice: "))
            if ach==6:
                break
            elif ach==1:
                os.system('cls')
                print("\tAnna Centenary Library")
                auser=input("Enter your email I'd: ")
                apassword=int(input("Creat your new password: "))
                aap={'mail':auser,'password':apassword}
                admin.append(aap)
                print("Admin has been added succesfully")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==2:
                os.system('cls')
                print("\tAnna Centenary Library")
                asub=input("Enter the subject of book: ")
                atitle=input("Enter the title of book: ")
                aref=input("Enter the Complete Reference: ")
                aauthor=input("Enter the Author name for the book: ")
                apublisher=input("Enter the Publisher: ")
                aed=int(input("Enter Edition of Book: "))
                apage=int(input("Enter total number of pages: "))
                aisbn=int(input("Enter the ISBN No. for book: "))
                acopy=int(input("Enter NO. of copies: "))
                acost=int(input("Enter cost of book: "))
                dbook={'sub':asub,'title':atitle,'Complete Reference':aref,'Author':aauthor,'Publisher':apublisher,'editon':aed,'page':apage,'ISBN':aisbn,'copies':acopy,'cost':acost,'Library':'Anna Centenary Library'}
                book.append(dbook)
                print(asub,"Book has been added succesfully")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==3:
                os.system('cls')
                print('\tAnna Centenary Library')
                rinput=input("Enter the Book Name to remove: ")
                for i in range(len(book)):
                    if book[i]['sub']==rinput:
                        del book[i]
                        print(rinput,"Book has been Romoved Succesfully")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        break
                else:
                    print(rinput,"Book  doest not have")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==5:
                os.system('cls')
                print('\tAnna Centenary Library') 
                showbook()
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==4:
                os.system('cls')
                print('\tAnna Centenary Library') 
                yz=input("Enter the book Name: ")
                change(yz) 
                input("--->>>PRESS ENTER TO CONTINUE<<<---")       
            else:
                os.system('cls')
                print("\t!!!INVALD USER NAME OR PASSWORD!!!")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
    elif choice==2:
        while True:
            os.system('cls')
            print("\tAnna Centenary Library")
            schoice=int(input("1.New Member\n2.Existing Member\n3.Close Membership\n4.Exit\nEnter your choice: "))
            if schoice==1:
                os.system('cls')
                print("\tAnna Centenary Library")
                sname=input("Enter student name: ")
                sroll=input("Enter student Roll No.: ")
                sbatch=int(input("Enter students batch: "))
                sbalane=int(input("Enter  minimum Rs.2000: "))
                smail=input("Enter student mail i'd: ")
                if(re.search(regex,smail)):   
                    print("Valid Email")  
                else:   
                    print("Invalid Email")  
                    break
                sph=int(input("Enter valid phone number: "))
                if sbalane<2000:
                    print("To get Library membership card you must pay atleat Rs.2000")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    break
                slist={'name':sname,'roll_no':sroll,'batch':sbatch,'balance':sbalane}
                students.append(slist)
                print(sname,"has succesfully registered for membership I'D")
                
                zz=zz+1
                print("\n*********************************************************************************************************************************************************************************************")
                print("\t\t\t\t\t\tAnna Centenary Library")
                print("\nMembership id: ",zz,"\tStudent name: ",sname,"\tRoll No.: ",sroll,"\tBatch: ",sbatch,"\tStudent mail id: ",smail,"\tStudent phone no.: ",sph,"\tMinimum Deposit: ",sbalane)
                print("Rules:")
                print("1.If a student failed to return the book within 15 Days he/she need to pay penalty Rs.2 per day\n2.If a student lost the book which is taken in library he/she need to pay due amount of 50 percentage of book cost\n3.If a student lost his/her library membership card they need to pay Rs.10 as penalty to get new membership card")
                print("***********************************************************************************************************************************************************************************************")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif schoice==2:                
                os.system('cls')
                print("\tAnna Centenary Library")
                ename=input("Enter your Name: ")
                epass=input("Enter your Roll No.: ")
                for i in students:
                    if ename==i['name'] and epass==i['roll_no']:
                        while True:
                            os.system('cls')
                            print("\tAnna Centenary Library")
                            print("\tWelcome",i['name'])
                            sch=int(input("1.Borrow Book\n2.Return Book\n3.Fine\n4.Checkout card\n5.Exit\nEnter your choice: "))
                            if sch==5:
                                break
                            elif sch==1:
                                os.system('cls')
                                print("\tAnna Centenary Library")
                                bbook=input("Choose book for borrow: ")
                                add.append(bbook)
                                print(bbook,"has succesfully added to cart")
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            elif sch==2:
                                os.system('cls')
                                print("\tAnna Centenary Library")
                                rbook=input("Enter book to return: ")
                                rfdate=input("Enter from date(DD/MM/YYYY): ")
                                rddate=input("Enter To date(DD/MM/YYYY):" )
                                rp=int(input("Enter count of penalty date: "))
                                rt={'book':tbook,'fdate':tfdate,'tdate':tddate,'penalty':rp}
                                r.append(rt)
                                take.remove(tt)
                                if rp!=0:
                                    aa=rp*2
                                    i['penalty']=aa
                                    late==aa
                                    print("Rs.",aa,"has been automatically deducted from your balance due to late submition")
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                else:
                                    print(tbook,"has beed succesfully returned")
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            elif sch==3:
                                while True:
                                    os.system('cls')
                                    print("\tAnna Centenary Library")
                                    pen=int(input("1.Lost book\n2.Lost Member ship id\n3.Exit\nEnter your choice: "))
                                    if pen==3:
                                        break
                                    elif pen==1:
                                        os.system('cls')
                                        print("\tAnna Centenary Library")
                                        for zzz in book:
                                            print(zzz['sub'],zzz['cost'])
                                            lbook=input("Enter lost book: ")
                                            lprice=int(input("Enter lost book price: "))
                                            z=lprice/2
                                            lostbook=z
                                            y=i['penalty']+z
                                            print("Rs",z,"amount has succesfully deducted from your account")
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    elif pen==2:
                                        os.system('cls')
                                        print("\tAnna Centenary Library")
                                        zzzz=i['penalty']+10
                                        # xy=zzzz+10
                                        yx=10
                                        lostmember=10
                                        print("Rs.",yx,"has succesfully deducted from your account")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            elif sch==4:
                                while True:
                                    os.system('cls')
                                    print("\tAnna Centenary Library")
                                    cardch=int(input("1.View to cart\n2.Remove from cart\n3.Exit\nEnter your choice: "))
                                    if cardch==1:
                                        os.system('cls')
                                        print("\tAnna Centenary Library")
                                        str1=" "
                                        os.system('cls')
                                        print("The book Succesfully saved in card:",str1.join(add))
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                        os.system('cls')
                                        print("\tAnna Centenary Library")
                                        by=int(input("1.Take\n2.Exit\nEnter your choice: "))
                                        if by==2:
                                            break
                                        elif by==1:
                                            os.system('cls')
                                            print("\tAnna Centenary Library")
                                            for xxx in book:
                                                print("\n",xxx['sub'])
                                                tbook=input("Enter book to take: ")
                                                tfdate=input("Enter from date(DD/MM/YYYY): ")
                                                tddate=input("Enter To date(DD/MM/YYYY):" )
                                                tt={'book':tbook,'fdate':tfdate,'tdate':tddate,'penalty':0}
                                                take.append(tt)
                                                print(tbook,"has beed succesfully borrowed")
                                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                        else:
                                            os.system('cls')
                                            print("Invalid input")
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    elif cardch==2:
                                        os.system('cls')
                                        print("\tAnna Centenary Library")
                                        if len(add)==0:
                                            print("No books in cart")
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                        else:
                                            reproduct=input("Enter the book name to remove from your Card: ")
                                            add.remove(reproduct)
                                            print(reproduct,"has been Removed from card Succesfully")
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    elif cardch==3:
                                        break
                                    else:
                                        print("Enter valid option")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif schoice==4:
                break
            elif schoice==3:
                os.system('cls')
                print("\tAnna Centenary Library")
                cname=input("Enter your Name: ")
                cpass=input("Enter your Roll No.: ")
                for j in students:
                    if cname==j['name'] and cpass==j['roll_no']:
                        os.system('cls')
                        print("\tAnna Centenary Library")
                        print("\tWelcome",j['name'])
                        aaa=j['balance']-j['penalty']
                        print("Rs.",aaa-500,"your amount has return to you succesfully ")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                # else:
                #     os.system('cls')
                #     print("User name not found")
                #     input("--->>>PRESS ENTER TO CONTINUE<<<---")
                for k in range(len(students)):
                    if students[k]['name']==cname:
                        del students[k]
                        print(cname,"has succesfully canclled your library membership")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        break   
                # else:
                #     print("error")
                #     input("--->>>PRESS ENTER TO CONTINUE<<<---")                
            else:
                os.system('cls')
                print("user name or password not found")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
    elif choice==3:
        exit()
    else:
       os.system('cls')
       print('\tAnna Centenary Library') 
       print("Invalid input")
       break
