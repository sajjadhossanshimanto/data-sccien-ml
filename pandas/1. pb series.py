# %%
import numpy as np
import pandas as pb

# %% Series
labels = ["a", "b", "c"]
my_list = [10, 20, 30]
arr = np.array(my_list)
d = {
    "a":10,
    "b":20,
    "c":30
}

#%%
pb.Series(data = my_list)
pb.Series(my_list)

# %%
pb.Series(my_list, index = labels)
pb.Series(my_list, labels)
# %% dict
pb.Series(d)

# %%
# any type of object is ok
pb.Series([sum, min, max])
# %%
ser1 = pb.Series([1, 2, 3, 4], index = ["bd", "in", "pk", "uk"])
ser1
# %%
ser2 = pb.Series([5, 6, 7, 8], index = ["it", "jp", "ge", "uk"])
ser2
# %% basics operations
ser1+ser2
# %%
