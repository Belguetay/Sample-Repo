import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3])

# Create a 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Create an array of zeros
zeros = np.zeros((2, 3))

# Create an array of ones
ones = np.ones((3, 2))

# Create an identity matrix
identity = np.eye(3)

print("1D Array:", arr1)
print("2D Array:", arr2)
print("Zeros Array:", zeros)
print("Ones Array:", ones)
print("Identity Matrix:", identity)

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
addition = a + b

# Element-wise multiplication
multiplication = a * b

# Reshape an array
c = np.array([1, 2, 3, 4, 5, 6])
reshaped = c.reshape(2, 3)

print("Addition:", addition)
print("Multiplication:", multiplication)
print("Reshaped Array:")
print(reshaped)