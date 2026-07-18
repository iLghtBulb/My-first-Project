import random

divisible_by_3 = []
not_divisible_by_3 = []

scores = [random.randint(1, 1000) for _ in range(100)]

for x in scores:
    if x % 3 == 0:
        divisible_by_3.append(x)
    else:
        not_divisible_by_3.append(x)

print("Durch 3 teilbar:")
print(divisible_by_3)
print("Anzahl durch 3 teilbar:", len(divisible_by_3))
print("Anzahl durch 3  nicht teilbar:", len(not_divisible_by_3))
print("Größte Zahl durch 3 telbar:", max(divisible_by_3))
print("Kleinste Zahl durch drei teilbar:", min(divisible_by_3))