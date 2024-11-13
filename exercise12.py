"""Ro'yxat berilga   x = ["olma", "banana", "olcha", "limon", "olxo'ri"]
Berilgan ro'yxat ichida 'o' harfidan boshlangan barcha elemetlarni chiqaring
"""
x = ["olma", "banana", "olcha", "limon", "olxo'ri"]

for meva in range(len(x)):

    if x[meva][0] == "o":
        print(x[meva])