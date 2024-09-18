#%%
import numpy as np

# %%
# list to array
l = list(range(9))
arr = np.array(l)
arr
# %%
l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
np.array(l)

# %%
# arange -> same to same as range except returns `np.array`
np.arange(0, 10)
np.arange(0, 11, 2)
# a range -> array range

# %%
# zeros -> [float_zero]
np.zeros(5)
np.zeros((3, 3))

# %%
# ones -> also float
a = np.ones(5)
# a.dtype
np.ones((2, 3))

# %%
# np.linspace -> float
# linearly siperated
# includes end point
np.linspace(0, 8, 5)
np.linspace(1, 13, 5)

# %%
# np.eye  ->  identity matrix
I3 = np.eye(3)
I3

# %%
# by dawing random we mean -> rant int in range 0->1
# but if we need to spacify range, use ....

np.random.rand(5)# 1D
np.random.rand(3, 2)# 2D

# %%
# "standard normal" distribution
# previous one was uniform distribution
np.random.randn(5)
np.random.randn(2, 3)

# %%
# randint -> rantdom num in range
# heigh end is exclusive 
np.random.randint(1, 100)
arr = np.random.randint(1, 100, 10)
arr
# %%
# methods
arr.max()
arr.min()
# %%
# ret -> index of min or max
arr.argmax()
arr.argmin()
# %%
arr.shape
# %%
# reshape -> is not inplace
arr.reshape(1, 10)
print(arr.reshape(10, 1))
print(arr)
# %%