n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

members = sorted(members, key=lambda x: (x[0]))

for i in members:
    print(i[0], i[1])
