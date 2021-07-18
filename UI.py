#!/usr/bin/env python
# coding: utf-8

# In[1]:


class QueryIn():
    status_of_existing_checking_account: str
    duration_in_month: int
    credit_history:	str
    purpose: str
    credit_amount: int
    savings_account_bonds:	str


# In[ ]:


from ml_utils import load_model,predictDict 
load_model()
print("====================================")
while True:
    print("Enter status_of_existing_checking_account\n"+str({'A14':"no checking account",'A11':"<0 DM", 'A12': "0 <= <200 DM",'A13':">= 200 DM "}))
    status_of_existing_checking_account=input()
    print("duration_in_month"+"\n 1 to 96")
    duration_in_month=int(input())
    print('credit_history\n'+str({"A34":"critical account","A33":"delay in paying off","A32":"existing credits paid back duly till now","A31":"all credits at this bank paid back duly","A30":"no credits taken"}))
    credit_history=input()
    print('purpose\n'+ str({"A40" : "car (new)", "A41" : "car (used)", "A42" : "furniture/equipment", "A43" :"radio/television" , "A44" : "domestic appliances", "A45" : "repairs", "A46" : "education", 'A47' : 'vacation','A48' : 'retraining','A49' : 'business','A410' : 'others'}))
    purpose=input()
    print('credit_amount\n'+str("0$ to 20000$"))
    credit_amount=int(input())
    print('savings_account_bonds\n'+str({"A65" : "no savings account","A61" :"<100 DM","A62" : "100 <= <500 DM","A63" :"500 <= < 1000 DM", "A64" :">= 1000 DM"}))
    savings_account_bonds=input()
    payload = {
        "status_of_existing_checking_account":status_of_existing_checking_account,   
        "duration_in_month": duration_in_month,
        "credit_history":credit_history,
        "purpose": purpose,
        "credit_amount": credit_amount,
        "savings_account_bonds": savings_account_bonds,
      }
    predictDict(payload)
    print("======================================")
    print("Try Again,[y/n]")
    ch=input()
    if(ch=='n'):
        break


# In[ ]:




