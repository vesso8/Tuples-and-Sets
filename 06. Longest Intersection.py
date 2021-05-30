n = int(input())
intersections = []
for _ in range(n):
    data = input()
    first_range , second_range = data.split("-")
    start, end = [int(el) for el in first_range.split(",")]
    first_seq = range(start, end+1)
    start, end = [int(el) for el in second_range.split(",")]
    second_seq = range(start, end + 1)
    intersection = set(first_seq).intersection(second_seq)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")