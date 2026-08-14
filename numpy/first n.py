#SECTION A - NUMPY ARRAYS
# 1.What is NumPy? Write any two advantages of using NumPy. 
#Answer
# NumPy (Numerical Python) is a Python library used for numerical and scientific computing. It provides a powerful data structure called an array for storing and processing numerical data.

# Two advantages:

# NumPy arrays are faster and more memory-efficient than Python lists for numerical operations.
# NumPy provides many mathematical and statistical functions for easy data processing.
# 2. Which function is used to create a NumPy array?
# #Answer 
# import numpy as np 
# arr = np.array([1, 2, 3, 4])
# print(arr)
# 3. Write a program to create a NumPy array containing numbers from 1 to 10.
#Answer
# import numpy as np

# arr = np.arange(1, 11)
# print(arr)
# 4. Create a NumPy array of even numbers from 2 to 20. 
#Answer
# import numpy as np 
# arr = np.array([10, 20, 30, 40])
# print(arr.dtype)
# 5. Create a NumPy array from the list [10,20,30,40,50].
#Answer
# import numpy as np

# arr = np.array([5, 10, 15, 20, 25])
# print(arr.size)
# 6. Write a program to print the datatype of a NumPy array. 
#Answer
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# 7. Find the number of elements in arr = np.array([5,10,15,20,25]). 
#Answer
# import numpy as np 
# arr = np.array([5, 10, 15, 20, 25]) 
# print(arr.size)
# 8. Write a program to create a 2D NumPy array of your choice. 
#Answer
# import numpy as np 
# arr = np.array([[1, 2, 3], [4, 5, 6]]) 
# print(arr)
# 9. Differentiate between Python List and NumPy Array (any 3 points).
#Answer
# Python List	                                            NumPy Array
# 1. Lists can store different types of data.	    #Arrays generally store elements of the same datatype.
# 2. Lists are slower for numerical calculations.	#NumPy arrays are faster for numerical calculations.
# 3. Lists use more memory for numerical data.	    #NumPy arrays are more memory-efficient.
# 10. Write a program to create an array of zeros of size 5.
#Answer
# import numpy as np
# arr = np.zeros(5)
# print(arr)
# Section B – Shape & Reshape
# 11. What is the purpose of the .shape attribute?
#Answer
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)
# 12. Find the shape of np.array([[1,2,3],[4,5,6]]).
#Answer
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)
# 13. Create an array from 1 to 12 and reshape it into a 3 x 4 matrix. 
#Answer
# import numpy as np

# arr = np.arange(1, 13).reshape(3, 4)
# print(arr)
# 14. Reshape np.arange(1,13) into a 2 x 6 matrix. 
# Answer
# import numpy as np

# arr = np.arange(1, 13).reshape(2, 6)
# print(arr)
# 15. What happens if reshape dimensions do not match the number of elements?
# #Answer 
# arr = np.arange(1, 7)
# arr.reshape(2, 4)

# 16. Convert a 1D array into a 2D array using reshape().
#Answer
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# new_arr = arr.reshape(2, 3)

# print(new_arr)
# 17. Create a 4 x 2 array using reshape().
#Answer
# import numpy as np

# arr = np.arange(1, 9).reshape(4, 2)
# print(arr)
# 18. Print both the original shape and reshaped shape of an array. 
#Answer
# import numpy as np

# arr = np.arange(1, 7)

# print("Original shape:", arr.shape)

# new_arr = arr.reshape(2, 3)

# print("Reshaped shape:", new_arr.shape)
# Section C – Join & Split Arrays
# 19. Which function is used to join two NumPy arrays? 
# import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# result = np.concatenate((arr1, arr2))
# print(result)
# 20. Join arr1=[1,2,3] and arr2=[4,5,6]. 
#Answer
# import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# result = np.concatenate((arr1, arr2))
# print(result)
# 21. Join two 2D arrays vertically.
#Answer
# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])

# result = np.concatenate((arr1, arr2), axis=0)
# print(result)
#  22. Join two 2D arrays horizontally.
#Answer
# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])

# result = np.concatenate((arr1, arr2), axis=1)
# print(result)
#  23. Dtifferentiate between concatenate() and stack().
#Answer
# np.concatenate((arr1, arr2))
# np.stack((arr1, arr2))
# 24. Which function is used to split a NumPy array? 
#Answer
# np.split()
# 25. Split np.array([1,2,3,4,5,6]) into 3 equal parts.
#Answer
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# result = np.split(arr, 3)
# print(result)
# 26. Split an array into 4 equal parts
#Answer
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# result = np.split(arr, 4)
# print(result)