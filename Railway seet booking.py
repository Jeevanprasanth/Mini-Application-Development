import os
import random
print("\tKPRIET RAILWAYS")
users=[{'mail':'jeevan@gmail.com','phone':1234567890,'user':"Jeevan",'password':1234,'Balance':500},
        {'mail':'prasanth20@gmail.com','phone':1234567890,'user':"Jeevan1",'password':1234,'Balance':1000},
        {'mail':'ohm@kpriet.ac.in','phone':1234567890,'user':"Jeevan2",'password':1234,'Balance':750}]
puser=[{'PNR':12345567890}]
c=[]
r=[]
w=[]
    #CBE TUP ED SA MAS
devil=[[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]
def booking():
    os.system('cls')
    print("\tKPRIET RAILWAYS")
    people = int(input("\nEnter no. of Ticket you want : "))
    if people<=40:
        name_l = []
        age_l = []
        sex_l = []
        bording_l=[]
        dispatch_l=[]
        
        for p in range(people):
            os.system('cls')
            print("\tKPRIET RAILWAYS")
            print("0.CBE\n1.TUP\n2.ED\n3.SA\n4.MAS")
            name = input("\nName : ")
            name_l.append(name)
            age  = int(input("\nAge  : "))
            age_l.append(age)
            sex  = input("\nMale or Female : ")
            sex_l.append(sex)
            bording=int(input("\nEnter the bording point: "))
            bording_l.append(bording)
            dispatch=int(input("\nEnter the Final Distination: "))
            dispatch_l.append(dispatch)
        restart = str(input("\nDid you forgot someone? y/n: "))
        devil[bording][dispatch]=1
        print(devil)
        if restart in ('y','YES','yes','Yes'):
            restart = ('Y')
        else :
            os.system('cls')
            print("\tKPRIET RAILWAYS")
            x = 0
            print("\nTotal Ticket : ",people)
            p1=None
            for p in range(1,people+1):
                p1=p
                print("\nTicket No: ",p1)
                print("Name : ", name_l[x])
                print("Age  : ", age_l[x])
                print("Sex : ",sex_l[x])
                print("Bording point: ",bording_l[x])
                print("Distination: ",dispatch_l[x])
                
                x += 1
                
                c.append(p1)
                c1=c[:10]
                print("Conform:",c1)
                if len(c)>10:
                    r.append(p1)
                    r1=r[:5]
                    print("RAC:",r1)
                    if len(r)>5:
                        w.append(p1)
                        w1=w[:5]
                        print("WAiting list:",w1)
                        if len(w)==5:
                            print("\nHouse full Ethu ku mela yaru varathiga mudila -- In Vadivelu version")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
    else:
        os.system('cls')
        print("\tKPRIET RAILWAYS")
        print("!!OOPS Sorry Passenger limit is 10 ")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")    
def cancelticket(c,r,w):
    os.system('cls')
    print("\tKPRIET RAILWAYS")
    while True:
        if len(c)==0 and len(r)==0 and len(w)==0:
            print("Passenger not booked the tickets yet")
            break        
        cancel=int(input("Enter the Ticket No. for cancel: "))
        a0=c.index(cancel)
        c[:10]
        r[:5]
        w[:5]
        if len(w)!=0 and len(r)!=0:
            
            
            c.remove(cancel)
            c.insert(a0,r[0])

            r.remove(r[0])
            
            r.append(w[0])

            
            w.remove(w[0])
            print("Ticket No.",cancel,"is succesfully cancalled")
            save=c[:10],r[:5],w[:5]
            print(c[:10],r[:5],w[:5])
            break
            
            
        elif len(r)!=0 and len(w)==0:
            c.remove(cancel)
            c.insert(a0,r[0])

            r.remove(r[0])
            
            print("Ticket No.",cancel,"is succesfully cancalled")
            save=c[:10],r[:5],w[:5]
            print(c[:10],r[:5],w[:5])
            break
        else:
            a1=c.remove(cancel)
            print("Ticket No.",cancel,"is succesfully cancalled")
            save=c[:10],r[:5],w[:5]
            print(c[:10],r[:5],w[:5])
            break
def bill(save):
    os.system('cls')
    print("\tKPRIET RAILWAYS")
    print("\n1 Lower: ",c[:10][0],"\n2 Lower: ",c[:10][1],"\n1 Middle: ",c[:10][2],"\n2 Middle: ",c[:10][3],"\n1 Upper: ",c[:10][4],"\n2 Upper: ",c[:10][5],"\n1 Side Lower: ",c[:10][6],"\n2 Side Lower: ",c[:10][7],"\n1 Side upper: ",c[:10][8],"\n2 Side upper: ",c[:10][9])
    input("--->>>PRESS ENTER TO CONTINUE<<<---")
def pnr():
    os.system('cls')
    print("\tKPRIET RAILWAYS")
    pnr=random.randint(10000000000,100000000000)
    print("Your PNR No.(Auto Generated)",pnr)
    input("--->>>PRESS ENTER TO CONTINUE<<<---")
while True:
    os.system('cls')
    print("\tKPRIET RAILWAYS")
    choice=int(input("1.New user\n2.Existing user\n3.Exit\nEnter your choice: "))
    os.system('cls')
    print("\tKPRIET RAILWAYS")
    if choice==1:
        os.system('cls')
        print("\tKPRIET RAILWAYS")
        nmail=input("Enter your mail id: ")
        nphone=int(input("Enter your phone number: "))
        nuser=input("Enter your user name: ")
        npassword=int(input("Enter your password: ")) 
        bap={'mail':nmail,'phone':nphone,'user':nuser,'password':npassword,'Balance':0}
        users.append(bap)
        print("Account has been created Succesfully")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
    elif choice==2:
        os.system('cls')
        print("\tKPRIET RAILWAYS")
        euser=input("Enter your user name: ")
        epassword=int(input("Enter your password: "))
        while True:
            b=None
            for k in users:
                if euser==k['user'] and epassword==k['password']:
                    b=k
            os.system('cls')
            print("Account loggedin succesfully",b)
            bpchoice=int(input("1.Booking Tickets\n2.Cancle the tickets\n3.Balance\n4.Generate Tickets\n5.Exit\n6.PNR\nEnter your Choice: "))             
            if bpchoice==5:
                break
            elif bpchoice==6:
                pnr()
            elif bpchoice==4:
                bill (c[:10])
                pass
            elif bpchoice==3:
                print("Your Balance is",b['Balance'])
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif bpchoice==2:
                cancelticket(c[:10],r[:5],w[:5])
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
            elif bpchoice==1:
                os.system('cls')
                print("\tKPRIET RAILWAYS")
                restart = ('Y')

                while restart != ('N','NO','n','no'):
                    booking()
                    print("\nYour Tickets are succesfully Booked!\nFrom Coimbatore to Chennai\n\tHappy Journy!")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    break
            else:
                os.system('cls')
                print("Account doesn't exisit")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
    elif choice==3:
        exit()
    else:
        os.system('cls')
        print("Invalid input")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
        break
