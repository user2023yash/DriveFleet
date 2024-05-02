import datetime,csv,pickle,sys,time,os
from prettytable import PrettyTable
from art import *
import car_module,customer_module
car = car_module.Car()
Cust = customer_module.customer()

class Main:
    
    def __init__(self):
        print("")
        self.animate_car()
        print("")
        print(":::====================================:: WELCOME TO CAR RENTAL PROGRAMME ::==================================:::")
        print("")
        i ="y"
        m = input("have added the admin_details file? (y/n):")
        if m == "y" or m == "Y":
            pass
        else:
            admin_file = open("admin_details.dat","w+")
            admin_file.close()
        while i =="y"or i=="Y":
            enter = input(":::> hello! sis/ma'am you wanna login as admin or a user:")
            if enter=="admin"or enter =="ADMIN":
                self.admin()
                i="n"
            else:
                if enter=="login"or enter=="LOGIN":
                    i = "n"
                    login_file = open('login_details.dat','rb+')
                    user_details = []
                    try:
                        while True:
                            reader = pickle.load(login_file)
                            user_details.append(reader)
                    except Exception:
                        login_file.close()
                    if user_details!=" ":
                        print(":::> please login before we enter the program")
                        self.login()
                    else:
                        print(":::> please add a user")
                        self.add_user()
                else:
                    print(":::> please enter 'admin' or 'user' for login in programme")
                    m = input(":::> wanna login again? (y/n):")
                    if m =="y"or m=="Y":
                        i="y"
                    else:
                        print("::=========Turning off programme=========::")

#admin mod
    def admin(self):                                            #[['yash', 'y123']]
        admin_file = open("admin_details.dat","rb+")
        admin_details = []
        try:
            while True:
                reader = pickle.load(admin_file)
                admin_details.append(reader)
                print("checking the file....")
                print(" ")
        except Exception:
            if len(admin_details)!=0:
                i = "y"
                while i =="y" or i =="Y":
                    admin_name = input("enter the admin name:")
                    admin_password = input("enter the password:")
                    for j in range(len(admin_details)):
                        if admin_details[j][0] == admin_name:
                            if admin_details[j][1] == admin_password:
                                print(":----------------------------------------------------------:")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                print("                ",f'Welcome back {admin_name}')
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                print(":----------------------------------------------------------:")
                                print(" ")
                                i = "n"
                                self.categories()
                                break
                        else:
                            print('========INCORRECT PASSWORD!=======')
                            i = str(input("Wanna try again? (y/n):"))  
                    else:
                        print(f':::> NO USER FOUND NAMED {admin_name}')
                        i = str(input(":::> Wanna try again? (y/n):"))
        
            else:
                print(":::> hello! sir/ma'am please add an admin:")
                self.add_admin()
            admin_file.close()
        
        
    def add_admin(self):#Final verified 1
        admin_name = str(input(":::> please enter admin name :"))
        print("hello! user",admin_name)
        admin_password = str(input(":::> please enter your password :"))
        admin_file = open('admin_details.dat','+rb')
        admin_details = []
        try:
            while True:
                reader = pickle.load(admin_file)
                admin_details.append(reader)    
        except Exception:
            pickle.dump([admin_name,admin_password],admin_file)
            print('====admin ADDED SUCCESSFULLY====')
            
        admin_file.close()

#user mod
    def login(self):#Final verified 1
        i = "y"
        while i == "y" or i == "Y":
            username = str(input(":::> please enter your username :"))
            print("hello! user",username)
            password = str(input(":::> please enter your password :"))
            login_file = open('login_details.dat','rb+')
            user_details = []
            try:
                while True:
                    reader = pickle.load(login_file)
                    user_details.append(reader)
            except Exception:
                login_file.close()
            for j in range(0,len(user_details)):
                if user_details[j][0] == username:
                    if user_details[j][1] == password:
                        print(":----------========================================---------:")
                        print(" ")
                        print("                ",f'Welcome back {username}')
                        print(" ")
                        print(":----------========================================---------:")
                        print(" ")
                        i = "n"
                        self.categories()
                        break
                    else:
                        print('====INCORRECT PASSWORD!====')
                        i = str(input(":::> Wanna try again? (y/n):"))
                        break
                elif len(user_details)-(j+1)>0:
                    j+=1   
                else:
                    print(f':::> NO USER FOUND NAMED {username}')
                    i = str(input(":::> Wanna try again? (y/n):"))
            
    #login()

#user mod
    def add_user(self):#Final verified 
        username = str(input(":::> please enter your username :"))
        print("hello! user",username)
        password = str(input(":::> please enter your password :"))
        login_file = open('login_details.dat','rb+')
        user_details = []
        try:
            while True:
                reader = pickle.load(login_file)
                user_details.append(reader)    
        except Exception:
            for i in user_details:
                if i[0] == username:
                    print(':::> USER ALREADY EXISTS')
                    break
                else:
                    pickle.dump([username,password],login_file)
                    print(':::> USER ADDED SUCCESSFULLY')
                
                login_file.close()
                a = input(":::> wanna login now? (y/n):")
                if a=="y"or a=="Y":
                    self.login()
                else:
                    print("::===============Turning off programme===============::")
#add_user()

    def animate_car(self):
        car = text2art("car_rental_sys")
        lines = car.split("\n")
        for i in range(50):
            for line in lines:
                print(" " * i + line)
            time.sleep(0.1)
            print("\033[H\033[J", end="")
            print(" ")
            print(" ")
            #print("\033c", end="")  # Clear the screen (works on Unix-like systems)
        # For Windows, you might need to use:
        # print("\033[H\033[J", end="")
        # However, it may not work in all environments

#animate_car()


# restart function in development------------------------
    def start(self):
        if not self.running:
            self.running = True
            print("programme started.")
            # Additional initialization code can be added here

    def stop(self):
        if self.running:
            self.running = False
            print("programme stopped.")
            # Additional cleanup code can be added here
    
    def exit(self):
        print("::=======================Exited the programme=================::")
        sys.exit()
    
    def restart(self):
        self.stop()
        self.start()


    def categories(self):
        table = PrettyTable(['CATEGORIES'],header = False,title = 'CATEGORIES')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
    
        table2.add_rows([['1. CAR MANAGEMENT'],
                        ['2. CUSTOMER MANAGEMENT'],
                        ['3. USER MANAGEMENT'],
                        ['4. RENT MANAGEMENT'],
                        ['5. BILL MANAGEMENT'],
                        ['6. SHUT DOWN']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)
        print("----------------------------------------------------------::")
        print(" ")
    
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the category no. :"))
            if choice == 1:
                i = "n"
                self.option1()
            elif choice == 2:
                i = "n"
                self.option2()
            elif choice == 3:
                i = "n"
                self.option3()
            elif choice == 4:
                i = "n"
                self.option4()
            elif choice == 5:
                i = "n"
                self.option5()
            elif choice == 6:
                i = "n"
                self.option6()
            else:
                print("=====ERROR!!!=====")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")
            
        
        #categories()
    

    def option1(self):
        table = PrettyTable(['options'],header = False,title = 'OPTIONS')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
        
        table2.add_rows([['1. Add car'],
                        ['2. Update car'],
                        ['3. Return car'],
                        ['4. Display car'],
                        ['5. Go back =>']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)
        print("----------------------------------------------------------::")
        print(" ")
    
    #['id','name','total','available','one_repair','on_rent','per_hour','per_day','per_week']
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the option no. :"))
                
            if choice == 1:           #verified
                i = "n"
                dct = {}
                while True:
                    id = input(":::> enter the id:")
                    if id != " ":
                        dct["id"]=id
                        break
                    else:
                        print(":::> ERROR!!! you must enter the id")
                        continue
                while True:
                    name = input(":::> enter the name:")
                    if name != " ":
                        dct["name"]=name
                        break
                    else:
                        print(":::> ERROR!!! you must enter the name")
                        continue
                while True:
                    total = input(":::> enter the total:")
                    if total != " ":
                        dct["total"]=total
                        break
                    else:
                        print(":::> ERROR!!! you must enter the total")
                        continue
                while True:
                    available = input(":::> enter the available car:")
                    if available != " ":
                        dct["available"]=available
                        break
                    else:
                        print(":::> ERROR!!! you must enter the available")
                        continue
                on_repair = input(":::> enter the car on repair:")
                if on_repair != " ":
                    dct["on_repair"]=on_repair
                else:
                    dct["on_repair"]=str(0)
                on_rent = input(":::> enter the cars on rent:")
                if on_rent != " ":
                    dct["on_rent"]=on_rent
                else:
                    dct["on_rent"]=str(0)
                
                while True:
                    print("1. for hour")
                    print("2. for day")
                    print("3. for week")
                    mod = input(":::> enter the mod on which car is rented:")
            
                    if mod == "1" or mod == "for hour" or mod == "hour":
                        per_hour = input(":::> enter the hours:")
                        if per_hour != " ":
                            dct["per_hour"]=per_hour
                            break
                        else:
                            if per_hour=="":
                                continue
                    elif mod == "2" or mod == "for day" or mod == "day":
                        per_day = int(input(":::> enter the days:"))
                        if per_day != " ":
                            dct["per_day"]=per_day
                            break
                        else:
                            if per_day =="":
                                continue
                    elif mod == "3" or mod == "for week" or mod == "week":
                        per_week = int(input(":::> enter the weeks:"))
                        if per_week != " ":
                            dct["per_week"]=per_week
                            break
                        else:
                            if per_week =="":
                                continue
                    
                car.add_car(dct)
                print("::-------------------------------------------------::")
                a = input(":::> wanna move back to options? (y/n):")
                if a =="y"or a=="Y":
                    self.option1()
            
            elif choice == 2:       #verified
                i = "n"
                dct = {}
                c_id = input(":::> enter the id in which you wanna make changes :")
                    
                id = input(":::> enter the id:")
                if id != " ":
                    dct["id"]=id
                else:
                    pass
                name = input(":::> enter the name:")
                if name != " ":
                    dct["name"]=name
                else:
                    pass
                total = input(":::> enter the total:")
                if total != " ":
                    dct["id"]=id
                else:
                    pass
                available = input(":::> enter the available car:")
                if available != " ":
                    dct["available"]=available
                else:
                    pass
                on_repair =input(":::> enter the car on repair:")
                if on_repair != " ":
                    dct["on_repair"]=on_repair
                else:
                    pass
                on_rent = input(":::> enter the cars on rent:")
                if on_rent != " ":
                    dct["on_rent"]=on_rent
                else:
                    pass
                while True:
                    print("1. for hour")
                    print("2. for day")
                    print("3. for week")
                    mod = input(":::> enter the mod on which car is rented:")
            
                    if mod == "1" or mod == "for hour" or mod == "hour":
                        per_hour = input(":::> enter the hours:")
                        if per_hour != " ":
                            dct["per_hour"]=per_hour
                            break
                        else:
                            if per_hour==" ":
                                continue
                    elif mod == "2" or mod == "for day" or mod == "day":
                        per_day = input(":::> enter the days:")
                        if per_day != " ":
                            dct["per_day"]=per_day
                            break
                        else:
                            if per_day ==" ":
                                continue
                    elif mod == "3" or mod == "for week" or mod == "week":
                        per_week = input(":::> enter the weeks:")
                        if per_week != " ":
                            dct["per_week"]=per_week
                            break
                        else:
                            if per_week ==" ":
                                continue
                        
                car.update_car(c_id,dct)
                print("::-------------------------------------------------::")
                a = input(":::> wanna move back to options? (y/n):")
                if a =="y"or a=="Y":
                    self.option1()
                
            
            elif choice == 3:   #not verified
                i = "n"
                user_detail = []
                rent_file = open('rent_details.csv','r',newline='')
                reader = csv.reader(rent_file)
                if reader != " ":                     #check it please
                    b = "y"
                    while b == "y" or b == "Y":
                        customer_id = input(":::> enter the customer id:")
                        for i in reader:
                            if i[0] == customer_id:
                                b = "n"
                                car.return_car(customer_id)
                                a = input(":::> wanna move back to options? (y/n):")
                                if a =="y"or a=="Y":
                                    self.option1()
                            else:
                                print("=====NO SUCH CUSTOMER ID EXISTS=====")
                                input(":::> Wanna ty again? (y/n):")
                    rent_file.close()
                else:
                    print("-------------ERROR!!!------------ ")
                    print("  .-(-_-)=> customer_details file is empty-----so please check if there is data there if not then add please")
                    x = input(":::> wanna go back to options? (y/n):")
                    if x =="y"or x=="Y":
                        self.option1()
                    else:
                        raise Exception("thanks! restart the program for more use")
                
            elif choice == 4:                   #verified
                i = "n"
                car_detail = []
                price_detail = []
                car_file = open('car_details.csv','r+',newline='')
                price_file = open('price_details.csv','r+',newline='')
                reader1 = csv.reader(car_file)
                reader2 = csv.reader(price_file)
                car_detail.append(reader1)
                price_detail.append(reader2)
                if car_detail !=" "or price_detail !=" ":                      
                    car.display_car()
                    a = input(":::> wanna move back to options? (y/n):")
                    if a =="y"or a=="Y":
                        self.option1()
                    else:
                        print("::--------------------------------------------------------------------------::")
                        
                else:
                    print(":=============ERROR!!!============:")
                    print("  .-(-_-)=> there is nothing to display......check if data is empty")
                    self.option1()

            elif choice == 5:
                i = "n"
                self.categories()
            
            else:
                print("::--------------------------------------------------::")
                print(":-------ERROR!!!-------:")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")
                if i =="n"or i=="N":
                    print("::<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>::")
            
        
    def option2(self):
        table = PrettyTable(['options'],header = False,title = 'OPTIONS')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
    
        table2.add_rows([['1. Add customer'],
                    ['2. Display customer'],
                    ['3. Go back =>']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)
        print("----------------------------------------------------------::")
        print(" ")
    
    #['Customer_id','Name','Phone_no.','Email_id']
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the option no. :"))
        
            if choice == 1:                        #verified
                i = "n"
                dct = {}
                Customer_id = input(":::> enter the customer id:")
                if Customer_id != " ":
                    dct["Customer_id"]=Customer_id
                else:
                    pass
                Name = input(":::> enter the customer name:")
                if Name != " ":
                    dct["Name"]=Name
                else:
                    pass
                Phone_no= input(":::> enter the customer phone no.:")
                if Phone_no != " ":
                    dct["Phone_no"]=Phone_no
                else:
                    pass
                Email_id= input(":::> enter the customer email id:")
                if Email_id != " ":
                    dct["Email_id"]=Email_id
                else:
                    pass
                Cust.add_customer(dct)
                a = input(":::> wanna move back to options? (y/n):")
                if a =="y"or a=="Y":
                    self.option2()
                else:
                    print("::--------------------------------------------------------------------------::")
                        
            
            elif choice == 2:                     #verified
                i = "n"
                customers_detail = []
                customers_details = open("customer_details.csv","r+",newline='')
                reader1 = csv.reader(customers_details)
                customers_detail.append(reader1)
                if customers_detail !=" ":                         
                    Cust.display_customer()
                    a = input(":::> wanna move back to options? (y/n):")
                    if a =="y"or a=="Y":
                        self.option2()
                    else:
                        print("::--------------------------------------------------------------------------::")
                        
                else:
                    print("============ERROR!!!============")
                    print("  .-(-_-)=> there is nothing to display......check if data is empty")
                    self.option2()
            
            elif choice == 3:
                i = "n"
                self.categories()
            else:
                print(":---------ERROR!!!---------:")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")
                if i=="n" or i=="N":
                    print("::<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>::")
            
        
    def option3(self):
        table = PrettyTable(['options'],header = False,title = 'OPTIONS')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
    
        table2.add_rows([['1. Add user'],
                    ['2. Go back =>']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)  
        print("----------------------------------------------------------::")
        print(" ")
    
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the option no. :"))
            if choice == 1:
                i = "n"
                self.add_user()
            elif choice == 2:
                i = "n"
                self.categories()
            else:
                print("----------ERROR!!!-----------")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")
                if i=="n" or i=="N":
                    print("::<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>::")

    def option4(self):
        table = PrettyTable(['options'],header = False,title = 'OPTIONS')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
    
        table2.add_rows([['1. Check car availability'],
                    ['2. Rent car'],
                    ['3. Go back =>']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)
        print("----------------------------------------------------------::")
        print(" ")
    
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the option no. :"))
            if choice == 1:
                i = "n"
                id = input("enter the car id:")
                number_of_cars = int(input(":::> enter the number of cars to be wanted:"))
                car.check_availability(id,number_of_cars)
                
            
            elif choice == 2:
                i = "n"
                lst = []
                id = input(":::> enter the car id for renting:")
                customer_id = input(":::> enter the customer id:")
                number_of_cars = int(input(":::> enter the no. of cars to be wanted:"))
                lst.append(customer_id)
                lst.append(id)
                lst.append(number_of_cars)
                j ="y"
                while j == "y"or j=="Y":
                    print("""
                    1. for hour or hours
                    2. for day or days
                    3. for week or weeks""")
                    mode= int(input(":::> enter the mode of renting car no. :"))
                    if  mode ==1 or mode ==2 or mode ==3:
                        lst.append(mode)
                        j ="n"
                        car.rent_car(lst)
                        print("::-------------------------------------------------::")
                        a = input(":::> wanna move back to options? (y/n):")
                        if a =="y"or a=="Y":
                            self.option4()
                    else:
                        print("-----ERROR!!!-----")
                        print("there is no option",mode)
                        l = input(":::> wanna enter mode again? (y/n):")
                        if l =="y":
                            pass
                        else:
                            j = "n"
            
            elif choice == 3:
                i = "n"
                self.categories()
            else:
                print("=====ERROR!!!=====")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")

    def option5(self):
        table = PrettyTable(['options'],header = False,title = 'OPTIONS')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
    
        table2.add_rows([['1. calculate bill and display it'],
                    ['2. Go back =>']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)
        print("----------------------------------------------------------::")
        print(" ")
    
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the option no. :"))
            if choice == 1:
                i = "n"
                
                car_file = open('car_details.csv','r+',newline='')
                price_file = open('price_details.csv','r+',newline='')
                reader1 = csv.reader(car_file)
                reader2 = csv.reader(price_file)
                o = "y"
                while o=="y"or o=="Y":
                    customer_id = input(":::> enter the customer id:")
                    for c,s in reader1,reader2:
                        if c[0]== customer_id or s[0]==customer_id:
                            o="n"
                            Cust.generate_bill(customer_id,datetime.datetime.now())
                        else:
                            print("------ERROR------")
                            print(":::> there is no data to calculate please check")
                            v = input(":::> wanna go back to options? (y/n)")
                            if v =="y"or v=="Y":
                                self.option5()
                            else:
                                print("::<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>::")
            elif choice == 2:
                i = "n"
                self.categories()
            else:
                print(":-----ERROR!!!-----:")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")
            
    def option6(self):
        table = PrettyTable(['options'],header = False,title = 'OPTIONS')
        table2 = PrettyTable(['FIELD'],border = False,header = False)
    
        table2.add_rows([['1. SHUT DOWN or EXIT'],
                        ['2. Go back =>']])
    
        table.add_row([table2])
        print(" ")
        print("----------------------------------------------------------::")
        print(table)  
        print("----------------------------------------------------------::")
        print(" ")
    
        i = "y"
        while i == "y" or i == "Y":
            choice = int(input(":::> Enter the option no. :"))
            if choice == 1:
                i = "n"
                self.exit()
            elif choice == 2:
                i = "n"
                self.categories()
            else:
                print("----------ERROR!!!-----------")
                print(":::> There is no option",choice)
                i = input(":::> Wanna try again? (y/n):")
                if i=="n" or i=="N":
                    print("::<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>::")

        

main = Main()


