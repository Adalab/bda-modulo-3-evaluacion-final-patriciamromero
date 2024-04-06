#1:

In stage 1, an initial exploration of the DataFrames "Activity" and "Loyalty" was conducted. The types of data in each column, the presence of null values and inconsistencies were observed. The columns "Points Redeemed", "Flights with Companions", "Dollar Cost Points Redeemed", "Salary", "Cancellation Year" and "Cancellation Month" were highlighted as important to review in future steps. Null values were detected in the columns "Salary" and "Cancellation Year/Month". The shape of both DataFrames was verified and descriptive statistics were collected. 

Main Activity data:

    Columns: 10
    Data type: Numeric (except "Dtype" which is object)
    Null values: None
    Relevant columns: "Points Redeemed", "Flights with Companions", "Dollar Cost Points Redeemed".
    Remarks:
    The first 5 rows of the columns "Points Redeemed", "Flights with Companions" and "Dollar Cost Points Redeemed" have value 0. Whether this is an error, origin or pattern will be analysed in detail.
    There're 1864 values duplicated. That were remove. 
    "Points Accumulated" has turned into integer. 


Main "Loyalty" data:
    Columns: 16
    Data type: Miscellaneous (integers, objects and floats).
    Null values: "Salary", "Cancellation Year" and "Cancellation Month".
    Relevant columns: "Salary", "Cancellation Year", "Cancellation Month".
    Remarks:
    The column "Salary" has many null values and could be converted to integer. As well as ther is a negative salary that must be transformed.
    The columns "Cancellation Year" and "Cancellation Month" have null values and are configured as floats, they should be integers.

The first thing to consider is the use and the information collected in both documents. In a first approach it is clear that 'Activity' tracks the activity of each customer, appearing at least 48 each Loyalty Number, the information collected in this DataFrame allows us to keep the activity updated for 'Flights Booked', 'Flights with Companions' and 'Total Flights', these columns are a summation of the previous values recording the flights taken by year and month. 

When merging information, we find duplicate values in 'Loyalty Number', as this can alter processing calculations. The null entries in 'Salary' are corrected before the documents are merged. These were the steps taken: 

1 - We turn positive the negative data. 
2 - We observe the data using a boxplot and a violinplot, which enable us to see the concentration and distribution of the data. In this way we can see that there are a large number of outliers.
3 - Examine the main statistic to fill the nulls with the most suitable data. As there are a large number of outliers, a comparison was made with the Iterative Imputer, comparing both with the original column values.  
4 - Filling nulls with mean as the resoult is the same rather using Iterative Imputer or not. 

Note: Other methods like KNN Imputer could also be a good approach to have more information to compare with, but it takes more time to process the data and there is a time limit for this project. Nevertheless, the code appears as commented, so if time or even computer characteristics are not a problem, we can use this method to compare as well. 

"Cancellation year" & "Cancellation month" columns:

Due to the high number of nulls, it was decided in this case to remove both of these columns. 

This information can be of huge value to the business, so a review of the process used to obtain this data to see if there are any errors in obtaining or updating this information would be highly recommended, as it may help to provide further information on customer behaviour. It would also be beneficial to investigate why these customers are cancelling their subscriptions. 

It was decided to merge the two DataFrames using the "Loyalty Number" column because it is common to both and because we understand that it is also a unique identifier for each passenger. A new csv collecting the information of both was created.

#2
1 - 
Observing the bar plotcreated we can confirm that there is a clear pattern for both years. The books increased significantlly for months 5 to 8 (May to August, both included) there's also a peak in December and in March. 
2 - Initially we can confirm that there is a relation between both columns as more distance more points accumulated. 

#3