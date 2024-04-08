#%%
# Import libraries for data manipulation and analysis
import pandas as pd

# Import libraries for visualization
import seaborn as sns
import matplotlib.pyplot as plt

#%%
# Define a color palette for consistency
palette="magma"

#%%
# Read data from CSV file
data = pd.read_csv("../files/out/data_merged.csv")

# Show the first few rows of the data
print(data.head())
#%%
# Configure plot size
plt.figure(figsize=(10, 6))

# Create bar chart to compare flights booked by month and year
sns.barplot(data=data, x='month', y='flights_booked', hue='year', palette=palette)
plt.title('Comparassion of flights booked each month years 2017 and 2018')
plt.xlabel('Month')
plt.ylabel('Quatinty')
plt.legend(title='Year')
plt.show()

#%%
data_pd= data.groupby(["loyalty_number"])[["points_accumulated", "distance"]].sum()
data_pd
#%%
sns.scatterplot(data_pd["points_accumulated"], data_pd["distance"], palette=palette)
plt.title("Scatterplot of Points Accumulated vs. Distance")
plt.xlabel("Points Accumulated")
plt.ylabel("Distance")
plt.show()

#%%
# Create countplot to show distribution of provinces
data_province= pd.DataFrame(data.groupby('province')["loyalty_number"].count())
type(data_province)
#%%
sns.countplot(data_province["province"], palette=palette)

# Rotate province labels for better readability
plt.xticks(rotation=90)

# Increase font size for labels
plt.xlabel("Province", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.show()

#%%
# Create bar chart to visualize average salary by education level
sns.barplot(x="education", y="salary", data=data, palette=palette)

# Rotate education level labels for better readability
plt.xticks(rotation=45)

# Increase font size for labels
plt.xlabel("Education level", fontsize=14)
plt.ylabel("Mean salary", fontsize=14)
plt.show()

#%%
# Count loyalty card holders by loyalty card type
df_cards = data.groupby("loyalty_card")["loyalty_number"].count().reset_index()

# Display loyalty card holder counts
print(df_cards)

# Create pie chart to visualize loyalty card distribution
plt.pie(
    "loyalty_number",
    labels="loyalty_card",
    data=df_cards,
    autopct="%1.1f%%",  # Format percentage labels with one decimal place
    colors=["pink", "royalblue", "salmon"],  # Use the defined palette for pie chart colors
    wedgeprops={"linewidth": 1, "edgecolor": "white"},  # Set border properties
    textprops={"fontsize": 8},  # Set font size for labels
    labeldistance= 0.8,  # Adjust label distance from pie chart
    startangle=90,  # Set starting angle for pie chart
    frame=True,  # Display pie chart with a frame
)
plt.show()

# %%
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Create the plot with clear dimensions
plt.figure(figsize=(10, 6))  # Set figure size for better readability

# Generate a count plot to visualize distributions
sns.countplot(
   x="marital_status",  # Specify the variable to group counts by
   hue="gender",  # Distinguish counts based on gender
   data=data,  # Provide the dataset containing the data
   palette=sns.color_palette("magma"),  # Set a visually appealing color scheme
)

# Add clear and descriptive labels for visual clarity
plt.title("Clients Distribution by Gender and Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Number of Clients")

# Enhance legend for better interpretation
plt.legend(title="Gender", title_fontsize=12, loc="upper right")  # Adjust for readability

# Display the generated plot
plt.show()



# %%
