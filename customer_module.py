import datetime,csv,pickle,os
from prettytable import PrettyTable

class customer:
    
    def __init__(self):
        pass
    
    #bill mod
    def calculate_bill(self,customer_id,time):#verified
        rent_file = open('rent_details.csv','r',newline='')
        price_file = open('price_details.csv','r',newline='')
    
        reader = csv.reader(rent_file)
        reader2 = csv.reader(price_file)
    
        v1 =[]
        price = 0
    
        for i in reader:
            if i[0] == customer_id:
                v1.extend(i)
    
        for i in reader2:
            if i[0] == v1[1]:
                if int(v1[3]) == 1:
                    price = int(i[1])
                elif int(v1[3]) == 2:
                    price = int(i[2])
                else:
                    price = [int(i[2]),int(i[3])]

        if int(v1[3]) == 1:
            if str(time)[:10] == v1[4][:10]:
                h = int(str(time)[11:13]) - int(v1[4][11:13])
                return(h*price),h
            else:
                d = int(str(time)[8:10]) - int(v1[4][8:10])
                h = abs(int(str(time)[11:13]) - int(v1[4][11:13]))
                if str(time)[11:13] < v1[4][11:13]:
                    return((d*24-h)*price),d*24-h
                else:
                    return((d*24+h)*price),d*24+h
            
        elif int(v1[3]) == 2:
            d1 = datetime.datetime.date(time)
            d2 = datetime.date(int(v1[4][:4]),int(v1[4][5:7]),int(v1[4][8:10]))
            d = d1-d2
            return(int(str(d)[:2])*price),int(str(d)[:2])
    
        elif int(v1[3]) == 3:
            d1 = datetime.datetime.date(time)
            d2 = datetime.date(int(v1[4][:4]),int(v1[4][5:7]),int(v1[4][8:10]))
            d = d1-d2
            w = int(str(d)[:2])//7
            d = int(str(d)[:2])%7
            return(w*price[1]+d*price[0]),(w,d)
        
    # inside calculate+bill function
    def generate_bill(self,customer_id,time):
        table = PrettyTable(['DRIVE FLEET'],header = True,title = 'BILL')
        table2 = PrettyTable(['FIELD','DETAILS'],border = False,header = False)
    
        rent_file = open('rent_details.csv','r',newline='')
        price_file = open('price_details.csv','r',newline='')
        customer_file = open('customer_details.csv','r',newline='')
        
        reader1 = csv.reader(rent_file)
        reader2 = csv.reader(price_file)
        reader3 = csv.reader(customer_file)
    
        v1 = []
        v2 = []
        v3 = []
    
        for i in reader1:
            if i[0] == customer_id:
                v1.extend(i)
        if v1 != []:
            for i in reader2:
                if i[0] == v1[1]:
                    v2.extend(i)
    
            for i in reader3:
                if i[0] == customer_id:
                    v3.extend(i)
    
            table2.add_rows([['CUSTOMER ID:',v3[0]],
                            ['NAME:',v3[1]],
                            ['PHONE:',v3[2]],
                            ['MAIL:',v3[3]]])
    
            if int(v1[3])  == 1:
                x,y = customer.calculate_bill(customer_id,time)
                table3 = PrettyTable(['ID','QTY','MODE','HOURS','PRICE','TOTAL'],border = False)
                table3.add_row([v1[1],v1[2],'HOURLY',y,v2[1],x])
            elif int(v1[3])  == 2:
                x,y = customer.calculate_bill(customer_id,time)
                table3 = PrettyTable(['ID','QTY','MODE','DAYS','PRICE','TOTAL'],border = False)
                table3.add_row([v1[1],v1[2],'DAILY',y,v2[2],x])
            elif int(v1[3])  == 3:
                x,y = customer.calculate_bill(customer_id,time)
                table3 = PrettyTable(['ID','QTY','MODE','WEEKS','PRICE','DAYS','PRICE','TOTAL'],border = False)
                table3.add_row([v1[1],v1[2],'WEEKLY',y[0],v2[3],y[1],v2[2],x])
    
            table._set_double_border_style()
            table3._set_columns_style()
            table.add_row([table2])
            table.add_row([''])
            table.add_row([table3])
            print(table)
    
    #customer mod
    def add_customer(self,dct):
        customer_file = open('customer_details.csv','a',newline='')
        writer = csv.writer(customer_file)
    
        l = ['Customer_id','Name','Phone_no','Email_id']
        v= []
        for i in dct:
            if i in l:
                v.append([i,dct[i]])
    
        if len(v) < len(l):
            for i in range(len(l)-len(v)):
                v.append(['',''])
    
        for i in range(len(l)): 
            for j in range(len(v)):
                if v[j][0] == l[i]:
                    v[j],v[i] = v[i],v[j]
                
        writer.writerow([i[1] for i in v])
        customer_file.close()
        print("--------customer successfully added--------")
        print("::-----------------------------------------------------::")
    
    #customer mod
    def display_customer(self):#to be verified
        table = PrettyTable(["Customer_id","Name","Phone_no","Email_id"])

        customers_details = open("customer_details.csv","r+",newline='')
        
        reader1 = csv.reader(customers_details)

        for i in reader1:
            table.add_row([i[0],i[1],i[2],i[3]])
            break
        print(table)
        customers_details.close()
        
cust = customer()