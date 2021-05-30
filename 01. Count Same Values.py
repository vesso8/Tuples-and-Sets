numbers = tuple([float(nums) for nums in input().split()])
nums_collector = {}

for number in numbers:
    if not number in nums_collector:
        nums_collector[number] = 0
    nums_collector[number] += 1

for key, value in nums_collector.items():
    print(f"{key} - {value} times")