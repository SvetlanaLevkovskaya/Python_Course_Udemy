even_sum = 0
for even_numbers in range(2, 101, 2):
    even_sum += even_numbers
print(even_sum)

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

