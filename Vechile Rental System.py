import os
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
admin=[{'mail':'jeevan@gmail.com','password':1234},
       {'mail':'hari@gmail.com','password':1234},
       {'mail':'ohm@gmail.com','password':1234}]
users=[{'mail':'jeevan@gmail.com','password':1234,'deposit':30000},
       {'mail':'hari@gmail.com','password':1234,'deposit':30000},
       {'mail':'ohm@gmail.com','password':1234,'deposit':30000}]
car=[{'name':'Audi A6','fuel':'73 L','power':'180 kW','count':10,'rent':50000,'run':0 },
     {'name':'A-Class Hatchbak','fuel':'70 L','power':'180 kW','rent':45000,'count':5,'run':0 },
     {'name':'Omni','fuel':'45 L','power':'85 kW','count':15,'rent':5000,'run':0 }]
bike=[{'name':'Hornet','edition':2019,'fuel':'30 L','count':8,'rent':5000,'run':0},
      {'name':'Activa 5G','edition':2020,'fuel':'25 L','count':7,'rent':3000,'run':0},
      {'name':'Splender','edition':2015,'fuel':'19 L','count':6,'rent':3500,'run':0}]
def returncar(ta2,uc):
    os.system('cls')
    print("\tROYALS")
    rcar=input("Enter car name to return: ")
    rdate=input("Enter return date: ")
    if ta2==rdate:
        rkm=int(input("No. of  driven Km : "))
        z=True
        if z==True:
            if rkm>500:
                for r in car:
                    if r['name']==rcar:
                        arkm1=r['rent']*0.15
                        arun0=r['run']+rkm
                        r['run']=arun0
                        r['count']=r['count']+1
                        break
                else:
                    os.system('cls')
                    print(rcar,"doesn't seems in retun car list")
                for e in users:
                    arkm2=e['deposit']-arkm1
                    e['deposit']=arkm2
                    print(arkm1,"has deducted from your security balance due to more KM travled ")
                    label=input("""Enter Car Damage as "LOW","MEDIUM","HIGH"\nEnter actual damage: """)
                    if label=="LOW":
                        label1=r['rent']*0.20
                        label2=e['deposit']-label1
                        e['deposit']=label2
                        uc.remove(rcar)
                        print(rcar,"has succesfully returned ")
                        print(e['deposit'],"has been succesfully refuned to you")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        z=False
                        break
                    elif label=="MEDIUM":
                        label3=r['rent']*0.50
                        label4=e['deposit']-label3
                        e['deposit']=label4
                        uc.remove(rcar)
                        print(rcar,"has succesfully returned ")
                        print(e['deposit'],"has been succesfully refuned to you")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        z=False
                        break
                    elif label=="HIGH":
                        label5=r['rent']*0.75
                        label6=e['deposit']-label5
                        e['deposit']=label6
                        uc.remove(rcar)
                        print(rcar,"has succesfully returned ")
                        print(e['deposit'],"has been succesfully refuned to you")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        z=False
                        break
                else:
                    os.system('cls')
                    print("invalid input from low med high")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            else:
                os.system('cls')
                print("your kM is less than 500")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
    else:
        os.system('cls')
        print("You failed to return car on date so your amount will not be return as per ruels")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
def returnbike(tab2,ub):
    os.system('cls')
    print("\tROYALS")
    rbike=input("Enter Bike name to return: ")
    rbdate=input("Enter return date: ")
    if tab2==rbdate:
        rbkm=int(input("Day driven Km : "))
        z=True
        if z==True:
            if rbkm>500:
                for a in car:
                    if a['name']==rbike:
                        asdf=a['rent']*0.15
                        arbun1=a['run']+rbkm
                        a['run']=arbun1
                        a['count']=a['count']+1
                        break
                else:
                    os.system('cls')
                    print(rbike,"doesn't seems in retun car list")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                for z in users:
                    aaa=z['deposit']-asdf
                    z['deposit']=aaa
                    print(asdf,"has deducted from your security balance due to more KM travled ")
                    label0=input("""Enter Car Damage as "LOW","MEDIUM","HIGH"\n Enter actual damage: """)
                    if label0=="LOW":
                        label10=a['rent']*0.20
                        label20=z['deposit']-label10
                        z['deposit']=label20
                        ub.remove(rbike)
                        print(rbike,"has succesfully returned ")
                        print(z['deposit'],"has been succesfully refuned to you")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        z=False
                        break
                    elif label0=="MEDIUM":
                        label30=a['rent']*0.50
                        label40=z['deposit']-label30
                        z['deposit']=label40
                        ub.remove(rbike)
                        print(rbike,"has succesfully returned ")
                        print(z['deposit'],"has been succesfully refuned to you")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        z=False
                        break
                    elif label0=="HIGH":
                        label50=a['rent']*0.75
                        label60=z['deposit']-label50
                        z['deposit']=label60
                        ub.remove(rbike)
                        print(rbike,"has succesfully returned ")
                        print(z['deposit'],"has been succesfully refuned to you")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        z=False
                        break
                else:
                    os.system('cls')
                    print("invalid input from low med high")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            else:
                os.system('cls')
                print("your kM is less than 500")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
    else:
        os.system('cls')
        print("You failed to return car on date so your amount will not be return as per ruels")
        input("--->>>PRESS ENTER TO CONTINUE<<<---")
uc=[]
ub=[]
lac=[]
lab=[]
while True:
    os.system('cls')
    print("\tROYALS")
    choice=int(input("1.Admin\n2.Users\n3.Exit\nEnter your Choice: "))
    if choice==1:
        os.system('cls')
        print("\tROYALS")
        email=input("Enter maili'd name: ")
        if(re.search(regex,email)):   
            print("Valid Email")  
        else:   
            print("Invalid Email")  
            break
        password=int(input("Enter your password: "))
        for i in admin:
            if email==i['mail'] and password==i['password']:
                break  
        else:
            os.system('cls')
            print("\t!!!INVALD USER NAME OR PASSWORD!!!")
            input("--->>>PRESS ENTER TO CONTINUE<<<---")
            break
        while True:
            os.system('cls')
            print("\t\t\tROYALS")
            print("\t---->>>>WELCOME TO ADMIN PAGE<<<<----")
            ach=int(input("1.List of vechile\n2.Search\n3.Edit Details\n4.Add Vechile\n5.Delete Vechile\n6.Service Vechile\n7.List of borrowed vechilce\n8.Exit\nEnter your choice: "))
            if ach==8:
                break
            elif ach==1:
                os.system('cls')
                print("\tROYALS")
                vch=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                os.system('cls')
                print("\tROYALS")
                if vch==1:
                    for i in car:
                        print("\nName of the car: ",i['name'],"\nFuel capacity: ",i['fuel'],"\nHourse power :",i['power'],"\nNumber of",i['name'],"Available: ",i['count'],"\nRent per day: ",i['rent'],"\nKilomerter run totally: ",i['run'])
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif vch==2:
                    for j in bike:
                        print("\nName of the bike: ",j['name'],"\nEdition: ",j['edition'],"\nFuel capacity :",j['fuel'],"\nNumver of",j['name'],"Available: ",j['count'],"\nRent per day: ",j['rent'],"\nTotal Kilometer run totally: ",j['run'])
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif vch==3:
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                else:
                    os.system('cls')
                    print("Invalid input from list of vechile in admin")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    break
            elif ach==2:
                os.system('cls')
                print("\tROYALS")
                scch=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                if scch==3:
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif scch==1:
                    os.system('cls')
                    print("\tROYALS")
                    sch=input("Enter Car name to search: ")
                    for k in car:
                        if k['name']==sch:
                            os.system('cls')
                            print("\tROYALS")
                            print("\nName of the car: ",k['name'],"\nFuel capacity: ",k['fuel'],"\nHourse power :",k['power'],"\nNumber of",k['name'],"Available: ",k['count'],"\nKilomerter run totally: ",k['run'])
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print(sch,"car not found")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif scch==2:
                    os.system('cls')
                    print("\tROYALS")
                    bch=input("Enter bike name to search: ")
                    for l in bike:
                        if l['name']==bch:
                            os.system('cls')
                            print("\tROYALS") 
                            print("\nName of the bike: ",l['name'],"\nEdition: ",l['edition'],"\nFuel capacity :",l['fuel'],"\nNumver of",l['name'],"Available: ",l['count'],"\nTotal Kilometer run totally: ",l['run'])
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print(bch,"Bike not found")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                else:
                    os.system('cls')
                    print("Invalid input from edit car")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==3:
                os.system('cls')
                print("\tROYALS")
                ech=int(input("1.Car\n2.Bike\n3.Exit\nEnter your Choice: "))
                if ech==3:
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif ech==1:
                    os.system('cls')
                    print("\tROYALS")
                    chacar=input("Enter the car name to modify detailis: ")
                    for m in car:
                        if m['name']==chacar:
                            os.system('cls')
                            print("\tROYALS")
                            print("\nName of the car: ",m['name'],"\nFuel capacity: ",m['fuel'],"\nHourse power :",m['power'],"\nNumber of",m['name'],"Available: ",m['count'],"\nKilomerter run totally: ",m['run'])
                            chcar=int(input("\nEnter the Count to change: "))
                            m['count']=chcar
                            print("\nName of the car: ",m['name'],"\nFuel capacity: ",m['fuel'],"\nHourse power :",m['power'],"\nNumber of",m['name'],"Available: ",m['count'],"\nKilomerter run totally: ",m['run'])
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print(chacar,"car not found")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif ech==2:
                    os.system('cls')
                    print("\tROYALS")
                    cbch=input("Enter bike name to search: ")
                    for n in bike:
                        if n['name']==cbch:
                            os.system('cls')
                            print("\tROYALS") 
                            print("\nName of the bike: ",n['name'],"\nEdition: ",n['edition'],"\nFuel capacity :",n['fuel'],"\nNumver of",n['name'],"Available: ",n['count'],"\nTotal Kilometer run totally: ",n['run'])
                            ch=int(input("Enter the count to change for bike: "))
                            n['count']=ch
                            print("\nName of the bike: ",n['name'],"\nEdition: ",n['edition'],"\nFuel capacity :",n['fuel'],"\nNumver of",n['name'],"Available: ",n['count'],"\nTotal Kilometer run totally: ",n['run'])
                            print(cbch,"Car has been added to list succesfully")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print(cbch,"Bike not found")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                else:
                    os.system('cls')
                    print("Invalid input from edit bike")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==4:
                os.system('cls')
                print("\tROYALS")
                a=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                if a==3:
                   input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif a==1:
                    os.system('cls')
                    print("\tROYALS")
                    acname=input("Enter care name: ")
                    acfuel=input("Enter Fuel Tank Capacity in L: ")
                    achorse=input("Enter Horse power in kW: ")
                    account=int(input("Enter number of count: "))
                    acrent=int(input("Enter rent amount per day: "))
                    ad={'name':acname,'fuel':acfuel,'power':achorse,'count':account,'rent':acrent,'run':0 }
                    car.append(ad)
                    print(car)
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif a==2:
                    os.system('cls')
                    print("\tROYALS")
                    abname=input("Enter Bike name: ")
                    abedition=int(input("Enter Edition of bike: "))
                    abfuel=input("Enter Fuel Tank Capacity in L: ")
                    abcount=int(input("Enter the number of count: "))
                    abrent=int(input("Enter rent amount per day: "))
                    adb={'name':abname,'edition':abedition,'fuel':abfuel,'count':abcount,'rent':abrent,'run':0}
                    bike.append(adb)
                    print(bike)
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                else:
                    os.system('cls')
                    print("Invalid input from admin add")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==5:
                os.system('cls')
                print("\tROYALS")
                dch=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                if dch==3:
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif dch==1:
                    os.system('cls')
                    print("\tROYALS")
                    dcar=input("Enter Car name to remove: ")
                    for o in range(len(car)):
                        if car[o]['name']==dcar:
                            del car[o]
                            print(dcar,"has been Romoved Succesfully")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print(dcar,"not found")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif dch==2:
                    os.system('cls')
                    print("\tROYALS")
                    dbike=input("Enter Bike name to remove: ")
                    for p in range(len(bike)):
                        if bike[p]['name']==dbike:
                            del bike[p]
                            print(dbike,"has been Romoved Succesfully")
                            print(bike)
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    else:
                        os.system('cls')
                        print(dbike,"not found")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==6:
                os.system('cls')
                print("\tROYALS")
                sec=int(input("1.car\n2.Bike\n3.Exit\nEnter your choice: "))
                if sec==1:
                    for aa in car:
                        if aa['run']>=3000:
                            os.system('cls')
                            print(aa['name'],"==>",aa['run'])
                            boost=int(input("\n1.Service\n2.Exit\nEnter your choice: "))
                            if boost==1:
                                aa['run']=0
                                print(aa['name'],"==>","servied: ",aa['run'])
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                break
                            elif boost==2:
                                break
                    else:
                        os.system('cls')
                        print("No Cars came for Service")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif sec==2:
                    for ab in bike:
                        if ab['run']>=1500:
                            os.system('cls')
                            print(ab['name'],"==>",ab['run'])
                            boost1=int(input("\n1.Service\n2.Exit\nEnter your choice: "))
                            if boost1==1:
                                ab['run']=0
                                print(ab['name'],"==>","servied: ",ab['run'])
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                break
                            elif boost==2:
                                break
                    else:
                        os.system('cls')
                        print("No Bike came for Service")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif sec==3:
                   input("--->>>PRESS ENTER TO CONTINUE<<<---")
            elif ach==7:
                os.system('cls')
                print("\tROYALS")
                brow=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                if brow==1:
                    if len(uc)>0:
                        str3=" "
                        print("\n",str3.join(uc))
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        break
                    else:
                        print("No car borrowed yet")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif brow==2:
                    if len(ub)>0:
                        str4=" "
                        print("\n",str4.join(ub))
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        break
                    else:
                        print("No car borrowed yet")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                elif brow==3:
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                else:
                    print("Invalid input from list of brrow vechiles in admin page")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
            else:
                os.system('cls')
                print("\tROYALS")
                print("Invalid input from addmin page")
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                break
    elif choice==2:
        while True:
            os.system('cls')
            print("\tROYALS")
            select=int(input("1.New user\n2.Existing user\n3.Exit\nEnter your choice: "))
            if select==3:
                break
            elif select==2:
                os.system('cls')
                print("\tROYALS")
                email=input("Enter maili'd name: ")
                if(re.search(regex,email)):   
                    print("Valid Email")  
                else:   
                    print("Invalid Email")  
                    break
                password=int(input("Enter your password: "))
                for i in users:
                    if email==i['mail'] and password==i['password']:
                        print("\t---->>>>WELCOME TO USER LOGIN<<<<----")
                        break  
                else:
                    os.system('cls')
                    print("\t!!!INVALD USER NAME OR PASSWORD!!!")
                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    break
                while True:
                    os.system('cls')
                    print("\tROYALS")
                    print("\t---->>>>WELCOME TO USER LOGIN<<<<----")
                    uch=int(input("1.Available Vechiles\n2.Choose Vechiles\n3.Check out\n4.Add amount\n5.Return Vechiles\n6.Exit\nEnter your choice: "))
                    if uch==1:
                        os.system('cls')
                        print("\tROYALS")
                        u1=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                        os.system('cls')
                        print("\tROYALS")
                        if u1==1:
                            for b in car:
                                if b['run']<3000 and b['count']>0:
                                    print("\nName of the car: ",b['name'],"\nFuel capacity: ",b['fuel'],"\nHourse power :",b['power'],"\nNumber of",b['name'],"Available: ",b['count'],"\nRent per day: ",b['rent'],"\nKilomerter run totally: ",b['run'])
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        elif u1==2:
                            for v in bike:
                                if v['run']<1500 and v['count']>0:
                                    print("\nName of the bike: ",v['name'],"\nEdition: ",v['edition'],"\nFuel capacity :",v['fuel'],"\nNumver of",v['name'],"Available: ",v['count'],"\nRent per day: ",v['rent'],"\nTotal Kilometer run totally: ",v['run'])
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        elif u1==3:
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        else:
                            os.system('cls')
                            print("Invalid input from list of vechile in admin")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    elif uch==2:
                        os.system('cls')
                        print("\tROYALS")
                        u2=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                        os.system('cls')
                        print("\tROYALS")
                        if u2==1:
                            os.system('cls')
                            print("\tROYALS")
                            ccar=input("Enter car name to choose: ")
                            for h in car:
                                if h['name']==ccar and len(uc)==0:
                                    uc.append(ccar)
                                    print(ccar,"has succusfully add to cart")
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    break
                            else:
                                os.system('cls')
                                print("Dear user you already choosen a car for ride") 
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        elif u2==2:
                            os.system('cls')
                            print("\tROYALS")
                            cbike=input("Enter car name to choose: ")
                            for u in bike:
                                if u['name']==cbike and len(ub)==0:
                                    ub.append(cbike)
                                    print(cbike,"has succusfully add to cart")
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    break
                            else:
                                os.system('cls')
                                print(cbike,"has not found in  car list") 
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        elif u2==3:
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        else:
                            os.system('cls')
                            print("error from add to cart")
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    elif uch==3:
                        os.system('cls')
                        print("\tROYALS")
                        u3=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                        os.system('cls')
                        print("\tROYALS")
                        if u3==1:
                            os.system('cls')
                            print("\tROYALS") 
                            if len(uc)==1:
                                str1=" "
                                print("Dear user you chosen",str1.join(uc))
                                t=int(input("1.Take\n2.Remove from cart\n3.Exit\nEnter your choice: "))
                                if t==3:   
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                elif t==1:
                                    bool=True
                                    for y in users:
                                        if bool==True:
                                            if y['deposit']>=10000:
                                                os.system('cls')
                                                print("\tROYALS")  
                                                tuc=y['mail'] 
                                                ta1=input("Enter car name: ")
                                                ta2=input("Enter Date to return: ")
                                                break
                                    else:
                                        os.system('cls')
                                        print(y['deposit'],"is less than Security deposit amount of 10000 so dear user you cann't able to take a car for ride")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    for g in car:
                                        if g['name']==ta1:
                                            os.system('cls')
                                            print("\tROYALS")
                                            lac.append(ta1)
                                            g['count']=g['count']-1
                                            print(ta1,"has succesfully checked out\nReturn car on: ",ta2,"\nRent per day: ",g['rent'])
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                            bool=False
                                            break
                                    else:
                                        os.system('cls')
                                        print("Car name not found in list try to enter correct name of the car")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    
                                elif t==2:
                                    os.system('cls')
                                    print("\tROYALS")
                                    rc=input("Enter Car name to remove from cart: ")
                                    for y in car:
                                        if y['name']==rc:
                                            uc.remove(rc) 
                                            print(rc,"has been succesfully removed from cart")
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                            break
                                    else:
                                        os.system('cls')
                                        print(rc,"not found in car list try to enter valid car name")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            elif len(uc)==0:
                                os.system('cls')
                                print("Dear user you haven't choose a car for ride")  
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            else:
                                print("Dear user you have already chosen a car for ride")  
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        if u3==2:
                            os.system('cls')
                            print("\tROYALS") 
                            if len(ub)==1:
                                str2=" "
                                print("Dear user you chosen",str2.join(ub))
                                x=int(input("1.Take\n2.Remove from cart\n3.Exit\nEnter your choice: "))
                                if x==3:   
                                    input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                elif x==1:
                                    bool1=True
                                    for c in users:
                                        if bool1==True:
                                            if c['deposit']>=3000:
                                                os.system('cls')
                                                print("\tROYALS")   
                                                tab1=input("Enter Bike name: ")
                                                tab2=input("Enter Date to return: ")
                                                break
                                    else:
                                        os.system('cls')
                                        print(c['deposit'],"is less than Security deposit amount of 3000 so Dear user you cant able to take a bike for ride")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    for t in bike:
                                        if t['name']==tab1:
                                            os.system('cls')
                                            print("\tROYALS")
                                            lab.append(tab1)
                                            t['count']=t['count']-1
                                            print(tab1,"has succesfully checked out\nReturn Bike on: ",tab2,"\nRent per day: ",t['rent'])
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                            bool1=False
                                            break
                                    else:
                                        os.system('cls')
                                        print("Bike name not found in list try to enter correct name of the Bike")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                    
                                elif x==2:
                                    os.system('cls')
                                    print("\tROYALS")
                                    rb=input("Enter Car name to remove from cart: ")
                                    for f in bike:
                                        if f['name']==rb:
                                            ub.remove(rb) 
                                            print(rb,"has been succesfully removed from cart")
                                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                                            break
                                    else:
                                        os.system('cls')
                                        print(rb,"not found in bike list try to enter valid bike name")
                                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            elif len(ub)==0:
                                os.system('cls')
                                print("Dear user you haven't choose a bike for ride")  
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            else:
                                print("Dear user you have already chosen a bike for ride")  
                                input("--->>>PRESS ENTER TO CONTINUE<<<---")
                    elif uch==4:
                        os.system('cls')
                        print("\tROYALS")
                        aamount=int(input("Enter amount to add in Security deposit amount:"))
                        for x in users:
                            a=x['deposit']+aamount
                            x['deposit']=a
                            print("you have add",aamount,"Succesfully to Security deposit ","\nyour new Security deposit amount: ",x['deposit'])
                            input("--->>>PRESS ENTER TO CONTINUE<<<---")
                            break
                    elif uch==6:
                        break
                    elif uch==5:
                        os.system('cls')
                        print("\tROYALS")
                        rv=int(input("1.Car\n2.Bike\n3.Exit\nEnter your choice: "))
                        if rv==1:
                            os.system('cls')
                            returncar(ta2,uc)
                        elif rv==2:
                            os.system('cls')
                            returnbike(tab2,ub)
                    else:
                        os.system('cls')
                        print("Invalid input from user login page")
                        input("--->>>PRESS ENTER TO CONTINUE<<<---")
                        break
            elif select==1:
                os.system('cls')
                print("\tROYALS")
                uname=input("Enter your name: ")
                umail=input("Enter your email id: ")
                if(re.search(regex,umail)):   
                    print("Valid Email")  
                else:   
                    print("Invalid Email")  
                    break
                upass=int(input("Enter your password: "))
                udeposit=int(input("Enter your Security Deposit Amount\nMinimum for car Rs.10000\nMinimum for Bike Rs.3000: "))
                ua={'name':uname,'mail':umail,'password':upass,'deposit':udeposit}
                users.append(ua)
                print(uname,"has succesfully registed as new user in ROYALS")
                print(users)
                input("--->>>PRESS ENTER TO CONTINUE<<<---")
            else:
                os.system('cls')
                print("Invalid input from user selection page")
    elif choice==3:
        exit()
    else:
        os.system('cls')
        print("\tROYALS")
        print("Invalid input from main loging page")
        print("\t---->>>>WELCOME TO ADMIN PAGE<<<<----")
