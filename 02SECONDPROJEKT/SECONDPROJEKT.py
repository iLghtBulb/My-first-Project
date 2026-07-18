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

# Deine Aufgabe ab hier:
# 1. Anzahl durch 3 teilbar ausgeben
# 2. Anzahl nicht durch 3 teilbar ausgeben
# 3. Größte Zahl aus divisible_by_3 ausgeben
# 4. Kleinste Zahl aus divisible_by_3 ausgeben