#1:

In stage 1, an initial exploration of the DataFrames "Activity" and "Loyalty" was conducted. The types of data in each column, the presence of null values and inconsistencies were observed. The columns "Points Redeemed", "Flights with Companions", "Dollar Cost Points Redeemed", "Salary", "Cancellation Year" and "Cancellation Month" were highlighted as important to review in future steps. Null values were detected in the columns "Salary" and "Cancellation Year/Month". The shape of both DataFrames was verified and descriptive statistics were collected. It was decided to join both DataFrames by using the column "Loyalty Number" because it is shared by both and because we understand that, in addition, it is a unique data that identifies each passenger.

Main Activity data:

    Columns: 10
    Data type: Numeric (except "Dtype" which is object)
    Null values: None
    Relevant columns: "Points Redeemed", "Flights with Companions", "Dollar Cost Points Redeemed".
    Remarks:
    The first 5 rows of the columns "Points Redeemed", "Flights with Companions" and "Dollar Cost Points Redeemed" have value 0. Whether this is an error, origin or pattern will be analysed in detail.


Main "Loyalty" data:
    Columns: 16
    Data type: Miscellaneous (integers, objects and floats).
    Null values: "Salary", "Cancellation Year" and "Cancellation Month".
    Relevant columns: "Salary", "Cancellation Year", "Cancellation Month".
    Remarks:
    The column "Salary" has many null values and could be converted to integer.
    The columns "Cancellation Year" and "Cancellation Month" have null values and are configured as floats, they should be integers.