#%%
# Import libraries for data manipulation and analysis
import pandas as pd

# Import libraries for visualization
import seaborn as sns
import matplotlib.pyplot as plt

#%%
# Define a color palette for consistency
palette = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
#%%
# Read data from CSV file
data = pd.read_csv("../src/files/data_merged.csv")

# Show the first few rows of the data
print(data.head())
#%%
# Configure plot size
plt.figure(figsize=(10, 6))

# Create bar chart to compare flights booked by month and year
sns.barplot(data=data, x='Month', y='Flights Booked', hue='Year', palette=palette)
plt.title('Comparassion of flights booked each month years 2017 and 2018')
plt.xlabel('Month')
plt.ylabel('Quatinty')
plt.legend(title='Year')
plt.show()

#%%
# Create scatterplot to visualize Points Accumulated vs. Distance
sns.scatterplot(data["Points Accumulated"], data["Distance"], palette=palette)
plt.title("Scatterplot of Points Accumulated vs. Distance")
plt.xlabel("Points Accumulated")
plt.ylabel("Distance")
plt.show()

#%%
# Create countplot to show distribution of provinces
sns.countplot(data["Province"], palette=palette)

# Rotate province labels for better readability
plt.xticks(rotation=90)

# Increase font size for labels
plt.xlabel("Province", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.show()

#%%
# Create bar chart to visualize average salary by education level
sns.barplot(x="Education", y="Salary", data=data, palette=palette)

# Rotate education level labels for better readability
plt.xticks(rotation=45)

# Increase font size for labels
plt.xlabel("Education level", fontsize=14)
plt.ylabel("Mean salary", fontsize=14)
plt.show()

#%%
# Count loyalty card holders by loyalty card type
df_cards = data.groupby("Loyalty Card")["Loyalty Number"].count().reset_index()

# Display loyalty card holder counts
print(df_cards)

# Create pie chart to visualize loyalty card distribution
plt.pie(
    "Loyalty Number",
    labels="Loyalty Card",
    data=df_cards,
    autopct="%1.1f%%",  # Format percentage labels with one decimal place
    colors=palette,  # Use the defined palette for pie chart colors
    wedgeprops={"linewidth": 1, "edgecolor": "white"},  # Set border properties
    textprops={"fontsize": 8},  # Set font size for labels
    labeldistance= 0.8,  # Adjust label distance from pie chart
    startangle=90,  # Set starting angle for pie chart
    frame=True,  # Display pie chart with a frame
)
plt.show()

# %%
