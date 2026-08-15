# 1. Create a DataFrame of 5 students.
#Answer 
import pandas as pd
data = { 
    "Name": ["Rahul", "Priya", "Aman", "Tamanna", "Shivani"],
      "Marks": [85, 90, 78, 65, 72]
} 
df = pd.DataFrame(data)
# print(df)
# 2. Display the first 3 rows.
#Answer
# print(df.head(3))
# 3. Display the last 2 rows.
#Answer
# print(df.tail(2))
# 4. Print only the Marks column.
#Answer
# print(df["Marks"])
# 5. Print Name and Marks together.
#Answer
# print(df[["Name","Marks"]])
# 6. Display the second row using loc[].
#Answer
# print(df.loc[2])
# 7. Display the third row using iloc[].
#Answer
# print(df.iloc[3])
# 8. Find the shape of the DataFrame.
#Answer
# print(df.shape)
# 9. Display the column names.
#Answer
# print(df["Name"])
# 10. Display the data types.
#Answer
# print(df.dtypes)
# 11. Sort students by marks in descending order.
# #Answer
# print(df.sort_values("Marks", ascending=False))
# 12. Add a new column named City.
#Answer
# df["City"] = ["Delhi", "Mumbai", "Chandigarh", "Sonipat", "Rothak"]

# print(df)
# 13. Remove the City column.
#Answer
# df = df.drop("City", axis=1)
# print(df)
# 14. Create a DataFrame with missing values.
#Answer
# data = {
#      "Name": ["Rahul", "Priya", "Aman", "Neha", "Rohit"],
#        "Marks": [85, None, 78, None, 72]
# }
# df = pd.DataFrame(data)
# print(df)
# 15. Replace missing values with 100.
#Answer
# print(df.fillna(100))
# 16. Remove rows with missing values.
#Answer
# print(df.dropna())
# 17. Convert all names to lowercase.
#Answer
# df["Name"] = df["Name"].str.lower()
# print(df)
# 18. Filter students with marks greater than 75.
#Answer
# print(df[df["Marks"] > 75])
# 19. Save the DataFrame as an Excel file.
#Answer
# df.to_excel("students.xlsx", index=False)
# print("Excel file saved successfully")
# 20. Create your own dataset and perform at least 10 Pandas operations.
#Answer
# import pandas as pd 
# # Create your own dataset
# data = {
#     "Name": ["Aman", "Priya", "Ravi", "Neha", "Karan"],
#     "Age": [20, 21, 19, 22, 20], 
#     "Marks": [85, 92, 68, 76, 88] 
# }
# df = pd.DataFrame(data)
# print(df)
