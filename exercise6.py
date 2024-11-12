"""List x = [1,2,3,4,5,6,6,7,8,9] berilgan list ichida 2 ga bo'linadiganlarni nechta ekanligini aniqlang."""

x = [1,2,3,4,5,6,6,7,8,9]
count= 0 
for i in x:
    if i % 2 == 0:
        count += 1
print(f"2 ga bo'linadiganla: {count}")