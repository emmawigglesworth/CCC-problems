#Telemarketer or not

ignore = False
first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
if first == 8 or first == 9:
    if second == third:
        if fourth == 8 or fourth == 9:
            ignore = True
if ignore:
    print("ignore")
else:
    print("answer")
