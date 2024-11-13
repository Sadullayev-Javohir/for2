""" 1 dan 100 gacha raqamlarni chop eting, lekin:
Agar raqam 3 ga bo'linadigan bo'lsa, "Fizz" ni chiqarin.
Agar raqam 5 ga bo'linadigan bo'lsa, "Buzz" ni chiqarin.
Agar raqam 3 va 5 ga ham bo'linadigan bo'lsa, "FizzBuzz" ni chiqarin"""
count = 0
for i in range(1, 100 + 1):
    # if i % 3 == 0:
    #     print("Fizz")
    # elif i % 3 == 0 and i % 5 == 0:
    #     print("FizzBuzz")
    # elif i % 5 == 0:
    #     print("Buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    count += 1
print(count)