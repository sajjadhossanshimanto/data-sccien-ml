#%%
import pandas as pd
import numpy as np

# %%
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
})
df
# %%
df.dropna()
# dangerious -> drop rows if any nan exists


# %%
df.dropna(axis=1)

# %%
df.dropna(thresh=2)

# %%
df.fillna(value="fill value")
# %%
df.fillna(value=0)

# %%
# sum(df['A']) # error
sum(df['A'].fillna(0))
# %%
