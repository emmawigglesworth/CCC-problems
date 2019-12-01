num = int(input())
possible = 0
hand = [1,2,3,4,5]
possible = 0
for x in range(len(hand)):
    firsthand = hand[x]
    for y in range(len(hand)):
        secondhand = hand[y]
        if firsthand+secondhand == num and firsthand !=0 and secondhand!=0:
            possible = possible + 1
            hand[x] = 0
            hand[y] = 0
if num<=5 and num>0:
    possible = possible + 1
print(possible)
