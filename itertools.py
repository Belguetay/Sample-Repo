from itertools import count
from itertools import chain
from itertools import combinations, permutations
from itertools import repeat

print("Experiment 1")
for i in count(start=1, step=2):
    if i > 10:
        break
    print(i)

# # # # #
print("Experiment 2")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = chain(list1, list2)

for item in combined:
    print(item)

# # # # #
print("Experiment 3")
elements = [1, 2, 3]
combination_result = combinations(elements, 2)
permutation_result = permutations(elements, 2)

for combo in combination_result:
    print("Combination:", combo)

for perm in permutation_result:
    print("Permutation:", perm)

# # # # #
print("Experiment 4")

for i in repeat("Hello", 3):
    print(i)