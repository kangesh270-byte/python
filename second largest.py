numbers = [12, 45, 7, 555, 23, 89, 56]

largest = numbers[0]
second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest Number:", second)