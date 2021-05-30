m , n = input().split()
m_set_numbers = set()
n_set_numbers = set()
for _ in range(int(m)):
    numbers = int(input())
    m_set_numbers.add(numbers)
for _ in range(int(n)):
    numbers = int(input())
    n_set_numbers.add(numbers)
result = m_set_numbers & n_set_numbers

print(*result, sep="\n")