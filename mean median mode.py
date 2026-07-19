numbers =[10,20,30,40,50]
#Mean
mean = sum(numbers) / len(numbers)
print("Mean:", mean)

#Median
numbers.sort()
median = numbers[len(numbers) // 2]
print("Median:", median)

#Mode
mode = max(numbers, key=numbers.count)
print("Mode:", mode)