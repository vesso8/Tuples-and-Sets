n = int(input())
car_data = set()
for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        car_data.add(number)
    else:
        if number in car_data:
            car_data.remove(number)
if car_data:
    [print(cars) for cars in car_data]
else:
    print("Parking Lot is Empty")

