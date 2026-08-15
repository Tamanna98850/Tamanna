# Question 1
# Question: Create a DataFrame using a dictionary.
# Solution:
# import pandas as pd

# data={"Name":["Rahul","Priya","Aman"],
#       "Marks":[85,90,78]}

# df=pd.DataFrame(data)
# print(df)
# Question 2
# Question: Display the first 2 rows using head().
# Solution:
# print(df.head(2))
# Question 3
# Question: Display the last row using tail().
# Solution:
# print(df.tail(1))
# Question 4
# Question: Find the shape of the DataFrame.
# Solution:
# print(df.shape)
# Question 5
# Question: Display all column names.
# Solution:
# print(df.columns)
# Question 6
# Question: Display data types of all columns.
# Solution:
# print(df.dtypes)
# Question 7
# Question: Display complete information about the DataFrame.
# Solution:
# df.info()
# Question 8
# Question: Display statistical summary.
# Solution:
# print(df.describe())
# Question 9
# Question: Print only the Name column.
# Solution:
# print(df['Name'])
# Question 10
# Question: Print Name and Marks columns.
# Solution:
# print(df[['Name', 'Marks']])


# Question 11
# Question: Print the second row using loc[].
# Solution:
# print(df.loc[1])
# Question 12
# Question: Print the third row using iloc[].
# Solution:
# print(df.iloc[2])
# Question 13
# Question: Display students whose Marks are greater than 80.
# Solution:
# print(df[df['Marks']>80])
# Question 14
# Question: Sort students by Marks.
# Solution:
# print(df.sort_values('Marks'))
# Question 15
# Question: Add a new column Grade.
# Solution:
# df["Grade"]=["A","A+","B"]
# print(df)
# Question 16
# Question: Remove the Grade column.
# Solution:
# df=df.drop("Grade",axis=1)
# print(df)
# Question 17
# Question: Replace missing values with 0.
# Solution:
# import pandas as pd

# data={"Name":["Rahul","Priya","Aman"],
#       "Marks":[85,None,78]}
# df=pd.DataFrame(data)
# print(df.fillna(0))
# Question 18
# Question: Remove rows containing missing values.
# Solution:
# print(df.dropna())
# Question 19
# Question: Convert all names to uppercase.
# Solution:
# df["Name"]=df["Name"].str.upper()
# print(df)
# Question 20
# Question: Save the DataFrame as a CSV file.
# Solution:
# df.to_csv("students.csv",index=False)
# print("File Saved Successfully")
# Assignment (Without Solutions)
# 1. Create a DataFrame of 5 students.
# 2. Display the first 3 rows.
# 3. Display the last 2 rows.
# 4. Print only the Marks column.
