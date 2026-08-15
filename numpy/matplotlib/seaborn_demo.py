# import seaborn as sns

# print(sns.__version__)

########## 1 ###########

# import matplotlib.pyplot as plt
# import seaborn as sns
# x = [1, 2, 3, 4, 5]
# y = [5, 7, 8, 7, 6]

# # Matplotlib
# plt.plot(x, y, color="red", marker="o", linestyle="--")
# plt.title("Matplotlib Example")
# plt.grid(True)
# plt.show()

# # Seaborn
# sns.set_style("darkgrid")
# sns.lineplot(x=x, y=y, marker="o")
# plt.title("Seaborn Example")
# plt.show()

############## 2 #########
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_style("darkgrid")
# sns.set_palette("dark")

# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 7, 9])

# plt.title("Styled with Seaborn")
# plt.show()

############# 3 #############
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# # Data
# data = {
#     "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "Marks": [20, 25, 35, 50, 60, 72, 78, 85, 88, 95],
#     "Gender": ["Male", "Female", "Male", "Female", "Male",
#                "Female", "Male", "Female", "Male", "Female"]
# }

# # DataFrame
# df = pd.DataFrame(data)

# # Style
# sns.set_style("whitegrid")

# # Scatter Plot
# sns.scatterplot(
#     data=df,
#     x="Hours_Studied",
#     y="Marks",
#     hue="Gender",
#     style="Gender",
#     s=50,
#     palette="bright"
# )

# # Labels and title
# plt.title("Hours Studied vs Marks by Gender")
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")

# plt.show()

####### 4 #########
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Exam scores
# scores = [55, 60, 65, 70, 70, 75, 75, 80, 85, 85,
#           85, 90, 92, 95, 100]

# # Style
# sns.set_style("whitegrid")

# # Histogram
# sns.histplot(
#     scores,
#     bins=7,
#     kde=True,
#     color="skyblue",
#     edgecolor="black"
# )

# # Title and labels
# plt.title("Distribution of Exam Scores")
# plt.xlabel("Score")
# plt.ylabel("Frequency")

# plt.show()

##### 5 ########
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# # Data
# data = {
#     "Gender": ["Male", "Female", "Male", "Female",
#                "Male", "Female", "Male", "Female"],
#     "Marks": [70, 85, 60, 90, 75, 88, 80, 92]
# }

# # DataFrame
# df = pd.DataFrame(data)

# # Style
# sns.set_style("whitegrid")

# # Boxplot
# sns.boxplot(
#     x="Gender",
#     y="Marks",
#     data=df,
#     palette="pastel",
#     width=0.5
# )

# # Title and labels
# plt.title("Marks Comparison: Male vs Female")
# plt.xlabel("Gender")
# plt.ylabel("Marks")

# plt.show()

########### 6 #######
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# # Data
# data = {
#     "Maths": [60, 70, 80, 90, 85],
#     "Science": [65, 75, 78, 92, 88],
#     "English": [58, 72, 80, 86, 83],
#     "Gender": ["Male", "Female", "Male", "Female", "Male"]
# }

# # DataFrame
# df = pd.DataFrame(data)

# # Style
# sns.set_style("whitegrid")

# # Pairplot
# sns.pairplot(
#     df,
#     hue="Gender",
#     palette="bright"
# )

# plt.suptitle("Pairplot of Subjects by Gender", y=1)

# plt.show()

########## 7 #########
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample Sales Data
# data = {
#     "Ads": [5, 10, 15, 20, 25, 30, 35],
#     "Sales": [50, 55, 65, 70, 80, 85, 95],
#     "Category": ["A", "B", "A", "B", "A", "B", "A"],
#     "Revenue": [200, 300, 400, 500, 600, 700, 800]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Style
# sns.set_style("whitegrid")

# # 1. Scatter Plot
# sns.scatterplot(
#     data=df,
#     x="Ads",
#     y="Sales",
#     hue="Category",
#     style="Category",
#     s=70
# )

# plt.title("Ads vs Sales by Category")
# plt.xlabel("Advertising")
# plt.ylabel("Sales")
# plt.show()


# # 2. Histogram
# sns.histplot(
#     data=df,
#     x="Revenue",
#     bins=4,
#     kde=True
# )

# plt.title("Revenue Distribution")
# plt.xlabel("Revenue")
# plt.ylabel("Frequency")
# plt.show()


# # 3. Boxplot
# sns.boxplot(
#     data=df,
#     x="Category",
#     y="Sales"
# )

# plt.title("Sales Comparison by Category")
# plt.xlabel("Category")
# plt.ylabel("Sales")
# plt.show()

