#!/usr/bin/env python
# coding: utf-8

# In[139]:


from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from credit_data_actual_values import substitute
from pandas import read_csv
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from sklearn.metrics import fbeta_score, f1_score,precision_score,recall_score,accuracy_score, roc_curve, auc
import copy
import pandas as pd


# In[5]:


clf = GradientBoostingClassifier()


# In[115]:


df=read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data",               sep=" ",header=None)
#Display first few rows in the data frame
df.head()


# In[102]:


def visualize(df):
    df_vis = copy.deepcopy(df)
    # Call the method substitute from credit_data_actual_values.py to display the real world values
    df_vis = substitute(df_vis)
    df_vis['Cost Matrix(Risk)'].value_counts().plot(kind='bar')
visualize(df)


# In[80]:


df= df.iloc[:, list(range(6)) + [-1]]
df


# In[157]:


# split the data frame into inputs and outputs
last_ix = len(df.columns) - 1
X = df.iloc[:,list(range(6))]
y= df.iloc[:,[-1]]
X


# In[154]:


# Categorical features has to be converted into integer values for the model to process. 
#This is done through one hot encoding.
# select categorical features
cat_ix = X.select_dtypes(include=['object', 'bool']).columns
print(cat_ix)
# one hot encode categorical features only
ct = ColumnTransformer([('o',OneHotEncoder(),cat_ix)], remainder='passthrough')
print(ct)
# enc = OneHotEncoder(handle_unknown='ignore')
# enc.fit(X)

# print(X)
X = ct.fit_transform(X)
# label encode the target variable to have the classes 0 and 1
y = LabelEncoder().fit_transform(y)
print(X.shape, y.shape, Counter(y))

print(X)


# In[106]:


#Splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)


# In[ ]:





# In[107]:


# function to train and load the model during startup
def load_model():
    # load the dataset from the official sklearn datasetsf
    
    # do the test-train split and train the model
    clf.fit(X_train, y_train)

    # calculate the print the accuracy score
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(acc)
    print(f"Model trained with accuracy: {round(acc, 3)}")
    #Calculating results for various evaluation metric
    precision = precision_score(y_test,y_pred, average='micro')
    recall = recall_score(y_test,y_pred, average='micro')
    accuracy = accuracy_score(y_test,y_pred)
    f1 = f1_score(y_test,y_pred, average='macro')
    print(f"Accuracy: {accuracy}")
    print(f"Recall: {recall}")
    print(f"Precision: {precision}")
    print(f"F1-score: {f1}")

load_model()


# In[160]:


def predict(query_data):
    return 1
    x = [list(query_data.values())]
    x=pd.DataFrame(x)
    print(x)
    cat_ix = X.select_dtypes(include=['object', 'bool']).columns
    print(cat_ix)
# one hot encode categorical features only
    ct = ColumnTransformer([('o',OneHotEncoder(),cat_ix)], remainder='passthrough')
    x = ct.fit_transform(x)
    print(x)
    prediction = clf.predict([x])[0]
    print(f"Model prediction: {classes[prediction]}")
    return classes[prediction]

query_data={
       "status_of_existing_checking_account": 'A11',
        "duration_in_month": '6',
        "credit_history":'A34',
        "purpose": 'A43',
        "credit_amount": '1169',
        "savings_account_bonds": 'A65',
      }
predict(query_data)


# In[ ]:




