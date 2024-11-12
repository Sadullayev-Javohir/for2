"""List berilgan mevalar = ['olma', 'banan', 'apelsin', 'olma']
Listning ichida nechta 'olma' so'z borligni aniqlang."""

mevalar = ['olma', 'banan', 'apelsin', 'olma']
count = 0
for meva in mevalar:
    if meva == 'olma':
        count += 1
print(count)