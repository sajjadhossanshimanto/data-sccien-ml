#%%
import numpy as np
import pandas as pd

# %%
np.random.seed(101)
np.random.randn(5, 4)# 5*4

# %%
pd.DataFrame(np.random.randn(5, 4))
# %%                                    5                         4
df = pd.DataFrame(
    np.random.randn(5, 4),
    index="a b c d e".split(),# 5
    columns='W X Y Z'.split()# 4 -> spelling "columns"
)
df
# %%
df["W"]
df["a"]# error
# %%
# df["W", "X"]# error
df[["W", "X"]]
# %%
df.W
# %%
# creating new column
df["total_wz"] = df["W"]+df["Z"]
# %%
df["total_wz"]


# to conclude -> in data frame indexing are column based


# %%
# df.drop("total_wz")# error -> axis not specified
# df.drop("total_wz", axis=1)# 1 -> col name
df.drop("a", axis=0)# 1 -> col name
# %%
df.drop("total_wz", axis=1)# error
# %%
df.loc['a']
# df.loc['w']# error
# %%
df.loc['a', 'W']
# %%
df.loc[["a", "b"], ["W", "X"]]# wow supports multi selection
# %%
df["W", "a"]# error
# %% contitional
df[df>0]
df>0
# %%
df["W"]>0# although size is not same
df[df["W"]>0]# no error
# %% two condition
df[ (df["W"]>0) & (df["X"]<0) ]
df[ df["W"]>0 & df["X"]<0 ]# error
# %% set new index
df.reset_index()
df.reset_index(inplace=True)
# not in placed
# %%
df.set_index("W")
# not in placed
# %%



# Index Levels
outside = ['G1','G2']# Error -> musst matcha the shape 
inside = [1,2,3,1,2,3]
hier_index = list(zip(inside, outside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index
#%%
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index
#%%
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df
# %%
