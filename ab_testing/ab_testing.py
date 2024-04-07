# %% Import libraries for data processing
# -----------------------------------------------------------------------
import pandas as pd  # Pandas for data manipulation and analysis in Python.

# Tratamiento de datos (Data Processing)
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Imputación de nulos usando métodos avanzados estadísticos (Imputation of missing values using advanced statistical methods)
# -----------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización (Visualization libraries)
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

from scipy import stats
from scipy.stats import shapiro, kstest
from scipy.stats import mannwhitneyu

#%%
palette="magma"

#%%
data = pd.read_csv("../files/out/data_merged.csv")

#%%

#%%
for col in data["education"].unique():
    print(f"Education level: {col}")
    print(data[data["education"] == col]["flights_booked"].describe())
    print("--------------------------------")

#%%
# Group data by education and calculate total flights booked, reset index for a DataFrame
df_filtered = pd.DataFrame(data.groupby('education')['flights_booked'].sum()).reset_index()

#%%

#%%
# Create a new column 'education_level' with categories based on education
df_filtered["education_level"] = df_filtered['education'].apply(lambda x: 'Sup Education' if x in ["Doctor", "Master"] else 'Low Education')
#%%

#%%
for level in df_filtered["education_level"].unique():
        print(level)
        print(f"The main statistics 'Flights Booked' for {level} are: ")
        print(df_filtered[df_filtered["education_level"] == level]["flights_booked"].describe().T)
# %%

#%%
# Create bar chart showing flights booked by education with 
sns.barplot(x="education",
            y="flights_booked",
            data=df_filtered,
            palette=palette)
plt.xticks(rotation=45);
# %%
# Create bar chart showing flights booked by education level 
sns.barplot(x="education_level",
            y="flights_booked",
            data=df_filtered,
            palette=palette);

plt.title("Flights booked for education level")
plt.xlabel("Education level")
plt.ylabel("Flights booked in total");

#%%
# Normality test using Kolmogorov-Smirnov test
p_value = kstest(data["flights_booked"], "norm").pvalue  # Kolmogorov-Smirnov test

alpha = 0.05

if p_value > alpha:
    print("Data belong to a normal distribution (p-value =", p_value, ")")
else:
    print("Data do not belong to a normal distribution (p-value =", p_value, ")")


# %%
