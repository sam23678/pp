import numpy as np
import pandas as pd
name=['nisma','amina','qqq','lll']
ages=[10,20,15,13]
x=list(zip(name,ages))
print(x)
df=pd.DataFrame(data=x,columns=['name','ages'])
print(df)
df=df.to_csv('newdata.csv',index=False)
ds=pd.read_csv('newdata.csv')
print(ds)
y=ds.head(2)
print(y)
x=ds['ages'].max()
print(x," is maximum age")
z=np.sort(ages)
print(z)
nd=pd.DataFrame(data=z,columns=['sorted_ages'])
nd.to_csv('newdata_sorted_ages.csv',index=False)