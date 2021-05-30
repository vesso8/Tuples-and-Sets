n = int(input())
unique_elements = set()
for _ in range(n):
    chemical_compounds = input().split()
    for elements in chemical_compounds:
        unique_elements.add(elements)
print('\n'.join(unique_elements))