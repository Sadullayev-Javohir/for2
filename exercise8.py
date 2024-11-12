""" 1 dan 100 gacha raqamlarni chop eting, lekin:
Agar raqam 3 ga bo'linadigan bo'lsa, "Fizz" ni chiqarin.
Agar raqam 5 ga bo'linadigan bo'lsa, "Buzz" ni chiqarin.
Agar raqam 3 va 5 ga ham bo'linadigan bo'lsa, "FizzBuzz" ni chiqarin"""

for i in range(100 + 1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
