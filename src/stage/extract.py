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
# %%
#Method to open files

def open_csv(rute):
  """
  Opens a CSV file and reads it into a pandas DataFrame.

  Args:
      rute(str): The path to the CSV file.

  Returns:
      pd.DataFrame: The DataFrame containing the data from the CSV file.
  """

  # Read the CSV file using pandas.read_csv
  df = pd.read_csv(rute)

  # Return the DataFrame
  return df
# %%
#%%
# Creation of a function to explore the DataFrames
def explore_df(df):
    """
    This function allows to make an initial data exploration. 

    Args:
      df (pandas.DataFrame): The DataFrame to explore. Refering to the ones previously opened. 

    Returns:
      None  
      """
    # Prints information about the DataFrame
    print("The main information for DataFrame is: ")
    df.info()
    print("______________________")
    # Print the first 5 rows of the DataFrame
    print(f"The first 5 rows for DataFrame are:")
    display(df.head())
# %%
# Define a function to obtain information about a DataFrame
def df_information(df):

    # Print the shape of the DataFrame (number of rows and columns)
    print(f"The shape for the DataFrame is: ")
    print(df.shape)
    print("_________________")

    # Print the list of column names
    print(f"The name of the columns are: {list(df.columns)}")
    print("_________________")

    # Print the number of null values in each column
    print(f"The number of nulls in the DataFrame:")
    print(df.isna().sum())
    print("_________________")

    # Print the number of duplicate rows in the DataFrame
    print(f"The number of values duplicated in the DataFrame:")
    print(df.duplicated().sum())
    print("_________________")

    # Print the transposed descriptive statistics (descriptive statistics for each column)
    print(f"The descriptive statistics for this DataFrame are:")
    display(df.describe().T) 
# %%
# Define a function to explore basic characteristics of each column in a DataFrame
def explore_columns(df):
   """
   Explores basic characteristics of each column in a DataFrame.

   Args:
       df (pd.DataFrame): The DataFrame to explore.

   Prints:
       Description of each column, including:
           - Number of values
           - Unique values
           - Data type
           - Number of null values
           - Number of duplicates
   """

   for column in df.columns:
       # Print a header for the current column
       print(f"-------- Exploring {column} --------")

       # Print the number of values in the column
       print(f"Number of values: {len(df[column].to_list())}")

       # Print the number of unique values in the column
       print(f"Unique values: {len(df[column].unique())}")

       # Print the data type of the column
       print(f"Data type: {df[column].dtypes}\n")

       # Print the number of null values in the column
       print(f"Total nulls: {df[column].isnull().sum()}")

       # Print the number of duplicate values in the column
       print(f"Duplicates: {df[column].duplicated().sum()}")

       # Add a space for readability
       print("__________________________")

# %%
