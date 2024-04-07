#%%
from sup import extract as e
from sup import transform_clean as t
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# %%
activity = e.open_csv("../files/input/Customer Flight Activity.csv")
loyalty = e.open_csv("../files/input/Customer Loyalty History.csv")
# %%
e.explore_df(activity)
e.explore_df(loyalty)
# %%
e.df_information(activity)
e.df_information(loyalty)
# %%
e.explore_columns(activity)
e.explore_columns(loyalty)
# %%
activity = activity.drop_duplicates()
# %%
t.filtering_nulls(activity)
# %%
t.filtering_nulls(loyalty)
# %%
loyalty["Salary"] = loyalty["Salary"].abs()
# %%
activity["Points Accumulated"] = activity["Points Accumulated"].astype(int)

#%% 
loyalty = loyalty.drop(columns=["Cancellation Year", "Cancellation Month"])

#%%
fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 5))

# Creates a boxplot on the first subplot
sns.boxplot(y = "Salary",
            data = loyalty, 
            width = 0.5, 
            color = "turquoise", 
            ax = axes[0])

axes[0].set_title("Boxplot usando la columna `salary'")



# Creates a violinplot on the second subplot
sns.violinplot(y = "Salary",
               data = loyalty, 
               width = 0.5, 
               color = "turquoise", 
               linewidth = 2, 
               ax = axes[1])


axes[1].set_title("Violinplot usando la columna `salary'")
# %%
loyal_copy = loyalty.copy()
# %%
loyal_copy['Salary_imputer'] = t.iterative_imputer(loyal_copy,'Salary')
# %%
# %%
loyal_copy.describe()[["Salary","Salary_imputer"]].T
# %%
loyalty["Salary"] = (loyalty["Salary"].fillna(loyalty["Salary"].mean())).astype(int)

# %%
df_all = activity.merge(loyalty, how='inner', on= "Loyalty Number")

# %%
t.standarize_column_names(df_all)
# %%
df_all.to_csv("../files/out/data_merged.csv")