import numpy as np

print("E X P E R I M E N T : 1")
# Create arrays
a = np.array([1, 2, 3])
b = 2

# Broadcasting: Multiply array 'a' by scalar 'b'
result = a * b

print("Result of Broadcasting:")
print(result)

# # # # #
print("E X P E R I M E N T : 2")
# Generate random integers between 1 and 100
random_integers = np.random.randint(1, 101, size=(3, 3))

# Generate random samples from a normal distribution
random_samples = np.random.normal(0, 1, 10)

print("Random Integers:")
print(random_integers)
print("Random Normal Samples:")
print(random_samples)

# # # # #
print("E X P E R I M E N T : 3")
# Generate random integers between 1 and 100
random_integers = np.random.randint(1, 101, size=(3, 3))

# Generate random samples from a normal distribution
random_samples = np.random.normal(0, 1, 10)

print("Random Integers:")
print(random_integers)
print("Random Normal Samples:")
print(random_samples)

# # # # #
print("E X P E R I M E N T : 4")
# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(A, B)

print("Matrix Multiplication:")
print(result)

# # # # #
print("E X P E R I M E N T : 5")
# Create an array
data = np.array([1, 2, 3, 4, 5, 2])

# Save the array to a file
np.save("data.npy", data)

# Load the array from the file
loaded_data = np.load("data.npy")

print("Loaded Data:")
print(loaded_data)