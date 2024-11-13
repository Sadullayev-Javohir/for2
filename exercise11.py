"""sonlar = [5, 10, 15, 20, 25, 30] berilgan ro'yxatning har bir elementini 3 ga
bo'lgandagi qoldiqni yangi ro'yxatga yuklang va hosil bo'lgan ro'yxatning elementlarini
 chiqaring"""

sonlar = [5, 10, 15, 20, 25, 30]
qoldiq = []

for son in range(len(sonlar)):

    if sonlar[son] % 3:
        qoldiq.append(sonlar[son] % 3)
        
print(qoldiq)