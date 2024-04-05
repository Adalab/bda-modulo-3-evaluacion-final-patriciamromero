#1:

In stage 1, an initial exploration of the DataFrames "Activity" and "Loyalty" was conducted. The types of data in each column, the presence of null values and inconsistencies were observed. The columns "Points Redeemed", "Flights with Companions", "Dollar Cost Points Redeemed", "Salary", "Cancellation Year" and "Cancellation Month" were highlighted as important to review in future steps. Null values were detected in the columns "Salary" and "Cancellation Year/Month". The shape of both DataFrames was verified and descriptive statistics were collected. It was decided to join both DataFrames by using the column "Loyalty Number" because it is shared by both and because we understand that, in addition, it is a unique data that identifies each passenger.

Main Activity data:

    Columns: 10
    Data type: Numeric (except "Dtype" which is object)
    Null values: None
    Relevant columns: "Points Redeemed", "Flights with Companions", "Dollar Cost Points Redeemed".
    Remarks:
    The first 5 rows of the columns "Points Redeemed", "Flights with Companions" and "Dollar Cost Points Redeemed" have value 0. Whether this is an error, origin or pattern will be analysed in detail.
    There're 1864 values duplicated.


Main "Loyalty" data:
    Columns: 16
    Data type: Miscellaneous (integers, objects and floats).
    Null values: "Salary", "Cancellation Year" and "Cancellation Month".
    Relevant columns: "Salary", "Cancellation Year", "Cancellation Month".
    Remarks:
    The column "Salary" has many null values and could be converted to integer. As well as ther is a negative salary that must be transformed.
    The columns "Cancellation Year" and "Cancellation Month" have null values and are configured as floats, they should be integers.

First of all we filter out the columns that have nulls, and display on the screen the percentage of nulls they hold. It is shown that the columns "Cancellation Year/Month" have a high percentage of nulls. On the other hand, "Salary" contains approximately 25% of nulls. In order to review one by one those columns the steps mentioned below were followed. Columns regarding cancellation have been processed together.
Salary column: 

1 - We turn positive the data that was negative. 
2 - We observe the data using a boxplot and a violinplot that allow us to see the concentration and distribution of the data. In this way we see that there are a large number of outliers.
3 - Explore the main statics in order to fill the nulls with the most suiatble data. As there is high number of outliers a comparasssion of KNN and Iterative Imputer was made, comparing both with the original column values. 
4 - Filling nulls with becasuse blabla


"Cancellation Year" & "Cancellation Month" column:

Due to the high number of nulls, it was decided in this case to remove both columns. 

This information may be of high value to the business, so a review of the process used to obtain this data to see if there are any errors in obtaining or updating this information would be highly recommended, as it may help to provide further information on customer behaviour. It would also be nice to investigate why these customers are cancelling their subscription. 