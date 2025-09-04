import pandas as pd     
import numpy as np         
x =pd.read_csv("filmtv_movies.csv")
#print(x.head(20))
#print(x.shape)
#print(x.columns)
#print(x.dtypes)
#print(x.describe())
#print(x.loc[:,'user_id'])
#print(x.loc[10:20,['app_name','user_id','review_id']])
#print(x.loc[x['user_gender']=='Female'])
#print(x.at[1,'review_id'])
"""x = x.groupby("user_id")
for user_id, i in x:
    print(f"user_id:{user_id}")
    print(x.head(5))"""
    
#y=x['user_gender'].replace('Female','human')
#print(y)

#print(x["review_id"].map({1:20,20:20}))
#print(x.loc[x['year'] >= 2010])
#print(x.loc[:,'title'])
#print(x.loc[10:20,['genre','avg_vote','country']])
#print(x.loc[(x['year'] >=2010) & (x['genre']=='drama')])
#print(x.iloc[3])
#print(x.iloc[3:5,0:4])
#print(x.at[1,'genre'])
#print([x['year'] >=2005])

#p=x.drop(labels='title',axis=1)
print(x.at[0,'year'] ==1990,inplace=True)
print(x.head(7))