import random

divisible_by_3 = []
scores = [random.randint(1, 1000) for _ in range(100)]
#The program generates 100 random integers between 1 and 1000 and stores them in a list called scores.
for x in scores:
    if x % 3 == 0:
        divisible_by_3.append(x)
print(divisible_by_3)
"""
The programm checks each number in the scores list to see if it is divisible by 3.
If a number is divisible by 3, it is added to the divisible_by_3 list.
Finally, the program prints the list of numbers that are divisible by 3.
"""
