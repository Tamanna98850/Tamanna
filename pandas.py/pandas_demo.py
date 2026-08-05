# Q - 1
#Create a Series from a list [5 , 10 , 15 , 20]and print it?
# import pandas as pd
# list = [5 , 10 , 15 , 20]
# series = pd.Series(list)
# print(series)
# print(series.to_string(index = False))

# Q-2
#Create a Series from the tuple (1 , 2 , 3 , 4)and print the second value using iloc?
# import pandas as pd
# tuple = (1 , 2 , 3 , 4)
# series = pd .Series(tuple)
# print(series.iloc[1])

#Q-3
#Create a Series a Dictonary{'A':10 , 'B':20 , 'C':30} and print the value for 'B' using loc?
# import pandas as pd
# data = {'A': 10,'B': 20,'C': 30}
# series = pd.Series(data)
# print(series.loc['B'])

#Q-4
#Update the value for 'C' to 35 using loc and print the series?
# import pandas as pd
# data = {'A': 10,'B': 20,'C': 30}
# series = pd.Series(data)
# series.loc['C'] = 35
# print(series)

#Q-5
#Filter and print all value greter than or equal to 20?
# import pandas as pd
# data = {'A': 10,'B': 20,'C': 35}
# series = pd.Series(data) 
# print(series[series >= 20])





