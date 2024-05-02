import datetime,csv,pickle,os
from prettytable import PrettyTable
import customer_module
customer = customer_module.customer()
class Car:
    
    def __init__(self):
        pass
        
    
    #car mod
    def add_car(self,dct:dict):#verified
        l1 = ['id','name','total','available','on_repair','on_rent']
        l2 = ['id','per_hour','per_day','per_week']
        v1 =[]
        v2 =[]
    
        for i in dct:
            if i == 'id':
                v1.append([i,dct[i]])
                v2.append([i,dct[i]])
            elif i in l1:
                v1.append([i,dct[i]])
            elif i in l2:
                v2.append([i,dct[i]])
            
        if len(v1) < len(l1):
            for i in range(len(l1)-len(v1)):
                v1.append(['',''])
    
        if len(v2) < len(l2):
            for i in range(len(l2)-len(v2)):
                v2.append(['',''])
    
        for i in range(len(l1)):
            for j in range(len(v1)):
                if v1[j][0] == l1[i]:
                    v1[i],v1[j] = v1[j],v1[i]
                    break
            
        for i in range(len(l2)):
            for j in range(len(v2)):
                if v2[j][0] == l2[i]:
                    v2[i],v2[j] = v2[j],v2[i]
                    break
    
        car_file = open('car_details.csv','a+',newline='')
        price_file = open('price_details.csv','a+',newline='')
    
        reader1 = csv.reader(car_file)
        writer1 = csv.writer(car_file)
        writer2 = csv.writer(price_file)
    
        for i in reader1:
            if reader1[0] == v1[0][1]:
                print('car_already exists')
                break
        else:
            writer1.writerow([x[1] for x in v1])
            writer2.writerow([x[1] for x in v2])
        
        car_file.close()
        price_file.close()
        print(":-----data successfully added-----:")

    #car mod
    def display_car(self):#verified
        table = PrettyTable(['id','name','total','available','one_repair','on_rent','per_hour','per_day','per_week'])
        
        car_file = open('car_details.csv','r+',newline='')
        price_file = open('price_details.csv','r+',newline='')

        reader1 = csv.reader(car_file)
        reader2 = csv.reader(price_file)
    
        for i in reader1:
            for j in reader2:
                if i[0] == j[0]:
                    table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],j[1],j[2],j[3]])
                    break

        car_file.close()
        price_file.close()
    
        print(table)

    #car mod
    def update_car(self,id,dct): #verified
        car_file = open('car_details.csv','r',newline='')
        price_file = open('price_details.csv','r',newline='')
        reader1 = csv.reader(car_file)
        reader2 = csv.reader(price_file)
    
        l1 = ['id','name','total','available','on_repair','on_rent']
        l2 = ['id','per_hour_R','per_day_R','per_week_R']
    
        v1 = []
        v2 = []
    
        for i in dct:
            if i == 'id':
                v1.append([i,dct[i]])
                v2.append([i,dct[i]])
            elif i in l1:
                v1.append([i,dct[i]])
            elif i in l2:
                v2.append([i,dct[i]])
            
        if len(v1) < len(l1):
            for i in range(len(l1)-len(v1)):
                v1.append(['',''])
    
        if len(v2) < len(l2):
            for i in range(len(l2)-len(v2)):
                v2.append(['',''])
    
        for i in range(len(l1)):
            for j in range(len(v1)):
                if v1[j][0] == l1[i]:
                    v1[i],v1[j] = v1[j],v1[i]
                    break
            
        for i in range(len(l2)):
            for j in range(len(v2)):
                if v2[j][0] == l2[i]:
                    v2[i],v2[j] = v2[j],v2[i]
                    break

        d1 = [i for i in reader1]
        d2 = [i for i in reader2]
    
        c1=[]
        c2=[]
    
        e = 0 
    
        for i in d1:
            if i[0] == id:
                e+=1
                l = []
                for j in range(len(v1)):
                    if v1[j][0] == '':
                        l.append(i[j])
                        continue
                    for k in l1:
                        if v1[j][0] == k :
                            l.append(v1[j][1])
                c1.append(l)       
            else:
                c1.append(i)

        for i in d2:
            if i[0] == id:
                l = []
                for j in range(len(v2)):
                    if v2[j][0] == '':
                        l.append(i[j])
                        continue
                    for k in l2:
                        if v2[j][0] == k :
                            l.append(v2[j][1])
                c2.append(l)
            else:
                c2.append(i)
    
        if e == 0:
            print('NO SUCH ID EXISTS') 
        
        car_file.close()
        price_file.close()
    
        car_file = open('car_details.csv','w',newline='')
        price_file = open('price_details.csv','w',newline='')
    
        writer1 = csv.writer(car_file)
        writer2 = csv.writer(price_file)
    
        writer1.writerows(c1)
        writer2.writerows(c2)
        
        car_file.close()
        price_file.close()
        print(":----data successfully updated----:") 

    #Rent mod 
    def check_availability(self,id,number_of_cars):#verified
        car_file = open('car_details.csv','r',newline='')
    
        reader = csv.reader(car_file)
    
        available = 0
    
        for i in reader:
            if i[0] == id:
                available = int(i[3])
        car_file.close()
        if available-number_of_cars >= 0:
            print(":-----available-----:")
            return True
            
        else:
            print("::--------------------------------------------------::")
            print(":::::",number_of_cars,"not available:::::")
            print("There are only",available,"available")
            print("::--------------------------------------------------::")
            return False
    
    #rent mod
    def rent_car(self,lst):#verified
        car_file = open('car_details.csv','r+',newline='')
        rent_file = open('rent_details.csv','a+',newline='')
    
        reader1 = csv.reader(car_file)
        writer = csv.writer(rent_file)
        
        customer_id = lst[0]
        id = lst[1]
        number_of_cars = lst[2]
        mode = lst[3]
        
        l=[]
        dct = {}
    
        if mode == 1:#hourly mode
            for i in reader1:
                if i[0] == id:
                    if self.check_availability(id,number_of_cars):
                        l.extend([customer_id,id,number_of_cars,mode,datetime.datetime.now()])
                        dct['available'] = (int(i[3])-number_of_cars)
                        dct['on_rent'] = (int(i[5])+number_of_cars)
                        
                
        elif mode == 2:#daily mode
            for i in reader1:
                if i[0] == id:
                    if self.check_availability(id,number_of_cars):
                        l.extend([customer_id,id,number_of_cars,mode,datetime.datetime.now()])
                        dct['available'] = (int(i[3])-number_of_cars)
                        dct['on_rent'] = (int(i[5])+number_of_cars)
                        

        elif mode == 3:#weekly mode
            for i in reader1:
                if i[0] == id:
                    if self.check_availability(id,number_of_cars):
                        l.extend([customer_id,id,number_of_cars,mode,datetime.datetime.now()])
                        dct['available'] = (int(i[3])-number_of_cars)
                        dct['on_rent'] = (int(i[5])+number_of_cars)
                        
    
        else:
            raise Exception('INCORRECT RENT MODE')
        
        print(l)
        writer.writerow(l)
        car_file.close()
        rent_file.close()
        self.update_car(id,dct)
        
    #car mod
    def return_car(self,customer_id):#verified
        rent_file1 = open('rent_details.csv','r',newline='')
        return_file = open('return_details.csv','a',newline='')
    
        reader2 = csv.reader(rent_file1) 
        writer2 = csv.writer(return_file)
    
        v1 = []
        v2 = []
    
        e = 0 
    
        for  i in reader2:
            if i[0] != customer_id:
                v1.append(i)
            else:
                v2.extend(i)
                x =customer.calculate_bill(customer_id,datetime.datetime.now())
                v2.extend([datetime.datetime.now(),x[0]])
    
    
    
        rent_file2 = open('rent_details.csv','w',newline='')
    
        writer1 = csv.writer(rent_file2)
        writer1.writerows(v1)
        rent_file2.close()
    
        car_file = open('car_details.csv','r',newline='')
        reader = csv.reader(car_file)
    
        dct = {}
        if v2 != []:
            writer2.writerow(v2)
            for i in reader:
                if i[0] == v2[1]:
                    dct['available'] = int(i[3])+int(v2[2])
                    dct['on_rent'] = int(i[5]) - int(v2[2])
            self.update_car(v2[1],dct)

        rent_file1.close()
        return_file.close()

car = Car()
#car.rent_car('cus123','thar123',10,1)