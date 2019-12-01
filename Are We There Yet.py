#Are We There Yet

distances = input().split()
for x in range(len(distances)):
    distances[x] = int(distances[x])
cities = [1,2,3,4,5]

for x in range(len(cities)):
    for y in range(len(cities)):
        total = 0
        if cities[x] - cities[y] == 1:
            total = distances[x-1]
        elif cities[y] - cities[x] == 1:
            total = distances[x]
        elif cities[x] == cities[y]:
            total = 0
        else:
            if cities[x] < cities[y]:
                for z in range(x,y):
                    total = total + distances[z]
            else:
                for z in range(y,x):
                    total = total + distances[z]
        print(total,end=" ")
    print()

##1 2   3    4 5
## 3  10  12  5
##
##3, city 2 to 1 is 3
##0, city 2 to 2 is 0 = 3 - 3
##10, city 2 to 3 is 10 
##22, city 2 to 4 is 10 + 12 = 22
##27, city 2 to 5 is  10 + 12 + 5 = 27
