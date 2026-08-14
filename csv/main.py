# import pandas as pd

# df = pd.read_csv(r"C:\Users\ADMIN\Desktop\Tamanna\csv\data.csv")

# print(df.head())
# #JSON file data import in python 
# # import json

# # with open("students.json", "r") as file:
# #     students = json.load(file)

# # print(students)
# import json
# from pathlib import Path

# file_path = Path(__file__).parent / "students.json"

# with open(file_path, "r") as file:
#     students = json.load(file)

# print(students)
# json data import in pandas
# import pandas as pd
# from pathlib import Path

# file_path = Path(__file__).parent / "students.json"

# df = pd.read_json(file_path)

# print(df)