#%%
# Import libraries for data processing
# -----------------------------------------------------------------------
import pandas as pd  # Pandas for data manipulation and analysis in Python.

# Optional libraries (can be removed if not used):
# -----------------------------------------------------------------------
# Import libraries for web scraping and data manipulation
# from bs4 import BeautifulSoup
# import requests

# Import libraries for web browser automation with Selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverManager manages the installation of the Chrome driver

# from selenium.webdriver.common.keys import Keys  # Keys is useful for simulating keyboard events in Selenium.
# from selenium.webdriver.support.ui import Select  # Select is used to interact with <select> elements on web pages.

# Import libraries for pausing execution
# -----------------------------------------------------------------------
# from time import sleep  # Sleep is used to pause the program execution for a number of seconds.

# Configurations
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None)  # Set a Pandas option to show all columns of a DataFrame.

import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)


pd.options.display.max_columns = None

pd.set_option('display.float_format', '{:.2f}'.format)

# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Imputación de nulos usando métodos avanzados estadísticos
# -----------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

from scipy.stats import shapiro
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind

#%%
data = pd.read_csv("../src/files/data_merged.csv")
# %%
df_filtered = data[["loyalty_number", "flights_booked", "education"]]

# %%
for category in data["education"].unique():
        
        df_filtered = data[data["education"] == category]
        print(f"Los principales estadísticos de la columna 'Flights Booked' para {category} son: ")
        print(df_filtered["flights_booked"].describe().T)
# %%
df_filtered["education_level"]= data['education'].apply(lambda x : 'Sup Education' if x in ["Doctor", "Master"] else 'Low Education')
# %%
for col in df_filtered["education_level"].unique():
    print(f"Education level: {col}")
    print(df_filtered[df_filtered["education_level"] ==  col]["flights_booked"].describe())
    print("--------------------------------")
# %%
sns.barplot(x = "education_level", y = "flights_booked", data = df_filtered, palette = "magma")

# %%
df_filtered["bookings"] = df_filtered["flights_booked"].apply(lambda num_bookings: "Low Flyer" if num_bookings <= 7 else "High Flyer")

#%%
df_filtered["bookings"] 
# %%
table = pd.crosstab(df_filtered["education_level"], df_filtered["bookings"]) 
table
# %%
table['High Flyer %'] = table['High Flyer'] / (table['High Flyer'] + table['Low Flyer']) * 100
table['Low Flyer %'] = table['Low Flyer'] / (table['High Flyer'] + table['Low Flyer']) * 100

table
# %%
# Cambiar nombres de variables

# Seleccionar paleta de colores
palette = "PRGn"

# Crear la figura y los subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))

# Gráfico de "Low Flyer"
sns.barplot(x=table.index, y="Low Flyer %", data=table, palette=palette, ax=axes[0])

# Gráfico de "High Flyer"
sns.barplot(x=table.index, y="High Flyer %", data=table, palette=palette, ax=axes[1])

# Añadir puntos con valores numéricos
#sns.pointplot(x=table.index, y="Low Flyer %", data=table, color='black', ax=axes[0])
#sns.pointplot(x=table.index, y="High Flyer %", data=table, color='black', ax=axes[1])

# Título principal y etiquetas
fig.suptitle("Rotación según Satisfacción General")
axes[0].set_title("Empleados que se quedaron")
axes[1].set_title("Empleados que se marcharon")
axes[0].set_xlabel("Grupo")
axes[0].set_ylabel("% de Empleados")
axes[1].set_xlabel("Grupo")

# Mostrar la figura
plt.show()
# %%
# Realizar la prueba de proporciones
chi2, p_value, _, _ = chi2_contingency(table)

# Imprimir el resultado de la prueba
alpha = 0.05
if p_value < alpha:
    print(f"Con un p_value de {p_value} hay una diferencia significativa")
else:
    print(f"Con un p_value de {p_value} no hay una diferencia significativa")
# %%
statistic, p_value = stats.shapiro(df_filtered['flights_booked'])
if p_value > 0.05:
        print(f"Para la columna 'flights_booked' los datos siguen una distribución normal.")
else:
        print(f"Para la columna 'flights_booked'los datos no siguen una distribución normal.")
# %%
