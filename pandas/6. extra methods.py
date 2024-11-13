#%%
import pandas as pd


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df
# %%
df.head()
#%%
df['col1'].unique()
# %%
df['col2'].value_counts()
# %%
df[df['col1']>2]
df[df['col2']==444]
df[(df['col1']>2) & (df['col2']==444)]
# %%
df['col1'].apply(lambda x: str(x).strip())
# %%
df['col3'].apply(len)
# %%
df['col1'].sum()
# %%
del df['col1']
# %%
df
# %%
df.columns
# %%
df.index
# %%
df.sort_values(by='col2')
# %%
df.isnull()
# %%
df.dropna()
# %%
import numpy as np

df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
# %%
df.fillna("0")
# %%
df.fillna("0")['col2'].apply(float).sum()

# %%
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df
# %%
df.pivot_table()# pari na
# %%
