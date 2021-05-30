n = int(input())
odd_numbers_set = set()
even_numbers_set = set()
for current_row in range(1, n + 1):
    name = input()
    sum_value = sum([ord(el) for el in name]) // current_row
    if sum_value % 2 == 0:
        even_numbers_set.add(sum_value)
    else:
        odd_numbers_set.add(sum_value)
sum_even_numbers = sum(even_numbers_set)
sum_odd_numbers = sum(odd_numbers_set)

if sum_odd_numbers == sum_even_numbers:
    union_values = [str(values) for values in odd_numbers_set.union(even_numbers_set)]
    print(', '.join(union_values))
elif sum_odd_numbers > sum_even_numbers:
    different_values = [str(values) for values in odd_numbers_set.difference(even_numbers_set)]
    print(', '.join(different_values))
else:
    symmetric_difference_values = [str(values) for values in odd_numbers_set.symmetric_difference(even_numbers_set)]
    print(', '.join(symmetric_difference_values))