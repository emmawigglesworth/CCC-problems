#Occupy Parking

spaces = int(input())
first = input()
second = input()

count = 0
for x in range(spaces):
    if first[x] == "C" and second[x] == "C":
        count = count + 1
print(count)
