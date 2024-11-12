"""Ekrandan matn kiritiladi masalan: “Welcome to System”  shu matn ichida nechta 
katta harf bor ekanligini aniqlang.
"""

text = input("Matn kiriting: ")

for i in text:
    if i.isupper():
        print(f"Katta harflar: {i}")