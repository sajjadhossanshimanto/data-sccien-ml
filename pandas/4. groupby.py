#%%
import numpy as np
import pandas as pd


data = {
    'Company': ['google', 'google', 'msft', 'msft', 'fb', 'fb'],
    'Person': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}
df = pd.DataFrame(data)
df
# %%
by_com = df.groupby('Company')
pd.DataFrame(by_com)
# %%
by_com.mean()
# %%
by_com.min()
# %%
by_com.max()

# %%
by_com.describe()
# %%
by_com.describe().transpose()

# %%
by_com.describe().transpose()["google"]

# %%
