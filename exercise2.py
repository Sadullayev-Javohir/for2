"""1 da 50 gacha bo'lgan toq va juft sonlarni yig'indisini hisoblash."""

toq = 0
juft = 0

for i in range(1, 50 + 1):
    if i % 2 == 0:
        toq += i
    else:
        juft += i
print(f"Toq: {toq}, Juft: {juft}")