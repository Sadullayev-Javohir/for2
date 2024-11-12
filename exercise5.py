"""A dan B gacha sonlar berilgan berilgan son ichida nechta toq va juft sonlar borligni aniqlang.
"""

A = int(input("A: "))
B = int(input("B: "))

toq = 0
juft = 0

for i in range(A, B + 1):
    if i % 2 == 0:
        toq += 1
    else:
        juft += 1

print(f"Toq sonlar soni: {toq}, Juft sonlari: {juft}")