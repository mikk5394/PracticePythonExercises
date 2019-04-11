import random

a = random.sample(range(1,30), 15)
b = random.sample(range(1,30), 17)

result = [i for i in a if i in b]

print(result)