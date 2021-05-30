number_of_guests = int(input())
regular_guests = set()
vip_guests = set()
all_guests = set()
for _ in range(number_of_guests):
    reservation_codes = input()
    all_guests.add(reservation_codes)
guests_at_party = input()
while not guests_at_party == "END":
    if guests_at_party in all_guests:
        all_guests.remove(guests_at_party)
    guests_at_party = input()
for guests in all_guests:
    if guests[0].isdigit():
        vip_guests.add(guests)
    else:
        regular_guests.add(guests)
print(len(all_guests))
for vip in sorted(all_guests):
    if vip[0].isdigit():
        print(vip)
        all_guests.remove(vip)
for regular in sorted(all_guests):
    if regular[0].isalpha():
        print(regular)