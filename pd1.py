#Code with dictionary
import pandas as pd
'''
DCT={'a':1,'b':2,'c':3,'d':4}

df=pd.Series(DCT)
print(df)'''
#dictonary with dataframe
'''
d1={'a':2,'b':4,'c':3}
d2={'a':4,'f':6,'c':7,'v':8}
data={'first':d1,'second':d2}
df=pd.DataFrame(data)

print(df)
'''
#when data contain ndarray
'''
Data=[[1,2,3],[3,5,7]]
df=pd.Series(Data)
print(df)
'''

#when data is a series

a=pd.Series([1,2,3,6,78,8])
a1=pd.Series([1.2,2.3,3.4,5.6,7.5,6.0])
s1=pd.Series(['a','s','f','g','h','j'])
data={'first':a,'second':a1,'third':s1}

df=pd.DataFrame(data)
print(df)