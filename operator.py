import operator

# # # # #
print("Experiment 1")

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_data = sorted(data, key=operator.itemgetter('age'))

print(sorted_data)

# # # # #
print("Experiment 2")

numbers = [5, 2, 9, 1, 7]
max_value = max(numbers)
min_value = min(numbers)

print("Maximum:", max_value)
print("Minimum:", min_value)

# # # # #
print("Experiment 3")

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result_add = list(map(operator.add, list1, list2))
result_sub = list(map(operator.sub, list1, list2))
result_mul = list(map(operator.mul, list1, list2))

print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)