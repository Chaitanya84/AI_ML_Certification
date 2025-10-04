import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# exploring the difference between python list and Numpy array


a = [1,2,3,4,5,6]
print("Python list is: ", a)
print(a*2)  # it will repeat the list two times

b = np.array(a)
print("Numpy array is: ", b)
print(b*2)  # it will multiply each element by 2

print(type(a))
print(type(b))

print("Array shape: ", b.shape)
print("Array mean: ", b.mean())

mat = b.reshape(2,3)
print ("Reshaped array: ", mat)  # it will give error because we have 5 elements in the array and we are trying to reshape it to 5*1 = 5 elements which is same as original array

print ("Transpose array: ", mat.T)  # it will not change anything because it is a 1D array
print("Access subset of array: ", mat[1:2, 0:2])  # it will give elements from index 1 to 3

mask = b > 3
print("Boolean mask: ", mask)  # it will give a boolean array where the condition is true
print("Accessing elements using boolean mask: ", b[mask])  # it will give elements where the condition is true

#adding arrays using bradcasting
a = np.array([[1],[4],[7]])
b = np.array([1,0,1])
print("Array a: ", a)
print("Array b: ", b)
print("Adding arrays a and b: ", a+b)  # it will add b to each row of a




