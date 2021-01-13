# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:08:27 2020

@author: Aditya Didwania
"""
    
import pandas as pd

#input amount of loan 
principal = input('Principal? ')
while principal.replace('.','',1).isdigit() is not True:
    print("Enter only Numbers")
    principal = input('Principal? ')

#input total payment made per month
payment = input('Payment? ')
while payment.replace('.','',1).isdigit() is not True:
    print("Enter only Numbers")
    payment = input('Payment? ')
    
#input interest rate, in decimal    
interest = input('Interest? ')
while interest.replace('.','',1).isdigit() is not True:
    print("Enter only Numbers")
    interest = input('Interest? ')

#input extra payment, if any
extra_payment = input('Extra Payment? ')
while extra_payment.replace('.','',1).isdigit() is not True:
    print("Enter only Numbers")
    extra_payment = input('Extra Payment? ')

#changing type of variables
principal=float(principal)
payment=float(payment)
interest=float(interest)
extra_payment=float(extra_payment)

#defining 1st row of all the required variables
month=1
start_principal=round(principal,2)
interest_paid=round(start_principal*interest/12,2)
principal_repaid=round(payment-interest_paid+extra_payment,2)  
end_principal=round(start_principal-principal_repaid,2)
total_principal_paid=round(start_principal,2)
total_interest_paid=round(interest_paid,2)
total_principal_repaid=round(principal_repaid,2)
total_payment=round(payment,2)


#create a list of required variables
table=[]
row = [month,start_principal,payment,interest_paid,extra_payment,principal_repaid,end_principal]
table.append(row)

#loop the variables defined above till the loan gets completely paid off
while round(end_principal,0)>0:
    row=[]
    month+=1
    start_principal=end_principal
    interest_paid=round(start_principal*interest/12,2)
    principal_repaid=round(payment-interest_paid+extra_payment,2)  
    end_principal=round(start_principal-principal_repaid,2)
    total_payment+=payment
    total_interest_paid+=interest_paid
    total_principal_repaid+=principal_repaid
    row = [month,start_principal,payment,interest_paid,extra_payment,principal_repaid,end_principal]
    table.append(row)

#creating dataframe using pandas
a=pd.DataFrame(table,columns=["month","start_principal","payment","interest_paid","extra_payment","principal_repaid","end_principal"])

#printing all the required data
print()
print(a)
print("Total_Payment:",round(total_payment,2))
print("Total_Interest_Paid:",round(total_interest_paid,2))
print("Total_Principal_Repaid:",round(total_principal_repaid,2))    
print("Years taken to repay loan:",month/12)





    

