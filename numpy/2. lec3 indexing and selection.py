#%%
import numpy as np

# %%
arr = np.arange(0, 11)
# %%
# list like indexing
arr[8]
arr[3:8]

# %%
# broadcating -> unique carecteristics
arr[2:7]=0
arr

# char every element
arr[:]=99
arr
# %% 2D
# list like
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr[1]
arr[1][2]
# %%
# np uique
arr[1, 2]

# partioal row and column selection
arr[:2, :2]
# %%
# conditional
arr = np.arange(11)
arr[arr>4]
# %%
