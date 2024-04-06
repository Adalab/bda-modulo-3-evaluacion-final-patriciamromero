
# %%import matplotlib.pyplot as plt
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

# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns




# Function to convert a column to a numeric data type (float or integer)
def convert_to_numeric(df, column, target_dtype="float"):
  """
  Converts a column to a numeric data type (float or integer) if possible.

  Args:
      df (pd.DataFrame): The DataFrame containing the column.
      column (str): The name of the column to convert.
      target_dtype (str, optional): The target numeric data type ("float" or "int"). Defaults to "float".

  Returns:
      pd.DataFrame: The DataFrame with the converted column (if successful).
  """

  # Check if values in the column can be converted to the target type
  if all(is_convertible(val, target_dtype) for val in df[column]):
    try:
      df[column] = pd.to_numeric(df[column], downcast=target_dtype)
      print(f"Column '{column}' successfully converted to {target_dtype}.")
    except:
      print(f"Failed to convert column '{column}' to {target_dtype}.")
  else:
    print(f"Values in column '{column}' cannot be entirely converted to {target_dtype}.")

  return df


# %%
# Function to convert a column to object data type (string)
def convert_to_object(df, column):
  """
  Converts a column to object data type (string).

  Args:
      df (pd.DataFrame): The DataFrame containing the column.
      column (str): The name of the column to convert.

  Returns:
      pd.DataFrame: The DataFrame with the converted column.
  """

  df[column] = df[column].astype('object')
  print(f"Column '{column}' converted to object.")

  return df

#%%
# Returns a list including the columns with nulls
def filtering_nulls(df):
    columns_with_nulls = []
    # Iterates through each column in the DataFrame
    for column in df.columns:
        # Check if the column has any null values using 'isnull().any()'
        if df[column].isnull().any():
            # If null are found, appends the column name to the list
            columns_with_nulls.append(column)
    # Returns the list of columns with nulls
    return columns_with_nulls

# %%
def iterative_imputer(df, column):
  """
  Imputes missing values in a column using an iterative imputer.

  Args:
      df (pd.DataFrame): The DataFrame containing the column.
      column (str): The name of the column to impute missing values.

  Returns:
      pd.Series: The imputed column.
  """
  imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)

 # ajustamos y tranformamos los datos
  imputer_iterative_imputado = imputer_iterative.fit_transform(df[[column]])

# comprobamos que es lo que nos devuelve, que en este caso es un array también
  return imputer_iterative_imputado

# %%
def standarize_column_names(df):
  """
  Standarize column names in a DataFrame by converting them to lowercase and replacing spaces with underscores.

  Args:
      df (pd.DataFrame): The DataFrame to modify.

  Returns:
      pd.DataFrame: The DataFrame with unified column names.
  """

  # Convert all column names to lowercase
  df.columns = df.columns.str.lower()  # Apply lowercase to all column names

  # Replace spaces in column names with underscores
  df.columns = df.columns.str.replace(" ", "_")  # Replace spaces with underscores

  return df
# %%
