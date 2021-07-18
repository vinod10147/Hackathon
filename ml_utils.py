#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


clf = GradientBoostingClassifier()


# In[3]:


df=read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data",               sep=" ",header=None)
#Display first few rows in the data frame
df.head()


# In[4]:


def visualize(df):
    df_vis = copy.deepcopy(df)
    # Call the method substitute from credit_data_actual_values.py to display the real world values
    df_vis = substitute(df_vis)
    df_vis['Cost Matrix(Risk)'].value_counts().plot(kind='bar')
#visualize(df)


# In[5]:


df= df.iloc[:, list(range(6)) + [-1]]
df


# In[6]:


# split the data frame into inputs and outputs
last_ix = len(df.columns) - 1
X = df.iloc[:,list(range(6))]
y= df.iloc[:,[-1]]
X


# In[7]:


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

print(X)
X = ct.fit_transform(X)
# label encode the target variable to have the classes 0 and 1
#y = LabelEncoder().fit_transform(y)
print(X.shape, y.shape, Counter(y))

print(y)


# In[8]:


#Splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)


# In[ ]:


# referred from h20 module(Model_Selection.ipynb)
importance = {
        "status_of_existing_checking_account": 0.45,
        "duration_in_month": 0.43,
        "credit_history": 0.25,
        "purpose": 0.45,
        "credit_amount": 0.41,
        "savings_account_bonds": 0.24
      }

# In[9]:


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


# In[11]:
def predictDict(query_data):
    x = [list(query_data.values())]
    x=pd.DataFrame(x)
    x = ct.transform(x)
    prediction = clf.predict(x)[0]
    print("Model prediction:", prediction)
    print("Based on these parameters "+ str(importance))
    if prediction == 1:
        print("Status: THIS PERSON IS ELIGIBLE FOR LOAN")
    else:
        print("Status: THIS PERSON IS NOT ELIGIBLE FOR LOAN")
    return prediction

def predict(query_data):
    x = [list(query_data.dict().values())]
    x=pd.DataFrame(x)
    print(x)
    print(cat_ix)
    x = ct.transform(x)
    print(x.shape)
    prediction = clf.predict(x)[0]
    print("Model prediction:", prediction)
    return prediction





# In[ ]:




