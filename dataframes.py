import pandas as pd    
import numpy as np          
data = {
    'name' :['arjun','rahul','nandini','kriska','kranthi','priya'],
    'Age':[23,24,21,24,25,26],
    'role':['editor','teacher','reader','writer','it','farmer'],
    'hobbies':['texting','cooking','leaning','playing','tennis','ragbbi'],
    'salary':[20000,23000,45000,21000,60000,30000]
}
data_frame = pd.DataFrame(data)


data2 = {
    'name' : ['arjun','rahul','nandini','kriska','kranthi','priya'],
    'ph.no':[234567889,1234567,138907890,4637809132,3457899255,456778956],
    
    
}
frame = pd.DataFrame(data2)

x =pd.merge(data_frame,frame,on = 'name')
print(x)