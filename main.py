import numpy as np
import pandas as pd
name=['nisma','amina','qqq','lll']
ages=[10,20,15,13]
x=list(zip(name,ages))
print(x)
df=pd.DataFrame(data=x,columns=['name','ages'])
print(df)
ds=pd.read_csv('newdata.csv')
print(ds)
y=ds.head(2)
print(y)
x=df['ages'].max()
print(x)
z=np.sort(ages)
print(z)
df.to_csv('newdata.csv',index=False)