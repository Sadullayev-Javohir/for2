"""sonlar = [5, 10, 15, 20, 25, 30]. Berilgan ro'yxatdagi faqat juft va 10 dan 
katta sonlarni olish.
"""

sonlar = [5, 10, 15, 20, 25, 30]

for son in range(len(sonlar)):
    if sonlar[son] % 2 == 0 and sonlar[son] > 10:
        print(sonlar[son])