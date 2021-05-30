text = input()
occurrences_collector = {}
for character in text:
    if not character in occurrences_collector:
        occurrences_collector[character] = 0
    occurrences_collector[character] += 1
for key , value in sorted(occurrences_collector.items()):
    print(f"{key}: {value} time/s")