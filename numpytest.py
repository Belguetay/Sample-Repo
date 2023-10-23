import numpy as np

print("E X P E R I M E N T : 1")
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

print("E X P E R I M E N T : 2")

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

print("E X P E R I M E N T : 3")
# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access a specific element
element3 = arr[0, 0]
element = arr[1, 2]
element2 = arr[1, 1]
# Slicing to get a subset
subset = arr[0:2, 1:3]

print(arr)
print("Element at [0, 0] of arr:", element3)
print("Element at [1, 2] of arr:", element)
print("Element at [1, 1] of arr:", element2)
print("Subset:")
print(subset)

print("E X P E R I M E N T : 4")
# Create an array
data = np.array([10, 20, 30, 40, 50])

# Calculate mean, median, and standard deviation
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print(data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)