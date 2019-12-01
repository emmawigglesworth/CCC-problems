days = int(input())
swifts = input().split()
for x in range(len(swifts)):
    swifts[x] = int(swifts[x])
sema = input().split()
for x in range(len(sema)):
    sema[x] = int(sema[x])

totalswift = 0
totalsema = 0
tieday = 0
for x in range(days):
    totalswift = totalswift + swifts[x]
    totalsema = totalsema + sema[x]

    if totalswift == totalsema:
        tieday = x+1
print(tieday)
