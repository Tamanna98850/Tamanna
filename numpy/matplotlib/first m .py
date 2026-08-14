# 1 What is Matplotlib?
#Answer
# Matplotlib is a Python library used to create
#  graphs and charts such as line graphs, bar graphs, pie charts, and scatter plots.
# 2. Which function is used to draw a line graph? 
#Answer
# plt.plot()
# 3. Plot X=[1,2,3,4,5], Y=[2,4,6,8,10]. 
#Answer
# import matplotlib.pyplot as plt
# X = [1,2,3,4,5]
# Y = [2,4,6,8,10]
# plt.plot(X,Y)
# plt.show()
# 4. Add title, X-axis label and Y-axis label to a line graph. 
#Answer
# import matplotlib.pyplot as plt
# X = [1,2,3,4,5]
# Y = [2,4,6,8,10]
# plt.plot(X,Y)
# plt.titel("Simple Bar Graph")
# plt.Xlable("X-axis")
# plt.Ylable("Y-axis")
# plt.show()

# 5. Draw a line graph showing marks of five students.
#Answer
# import matplotlib.pyplot as plt
# students = [1,2,3,4,5]
# marks = [2,4,6,8,10]
# plt.plot(students,marks,maker="o")
# plt.titel("Students Marks")
# plt.Xlable("Students")
# plt.Ylable("Marks")
# plt.show()

# 6. Plot two different lines on the same graph.
#Answer
# import matplotlib.pyplot as plt
# X = [1,2,3,4,5]
# Y = [2,4,6,8,10]
# Y2 = [1,3,5,7,9]
# plt.plot(X,Y1,Lable = "Line1")
# plt.plot(X,Y2,Lable = "Line2")
# plt.titel("Two Lines")
# plt.Xlable("X-axis")
# plt.Ylable("Y-axis")
# plt.legand()
# plt.show()
