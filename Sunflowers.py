#Sunflowers


def Rotate(rotation, table, flowers):
    rotation = []
    for x in range(flowers):
        onerow  = []
        for y in range(flowers-1,-1,-1):
            onerow.append(table[y][x])
        rotation.append(onerow)
    return(rotation)

def Check(table, flowers):
    for x in range(flowers-1):
        for y in range(flowers-1):
            if table[x][y] > table[x][y+1]:
                return False
            elif table[x][y] > table[x+1][y]:
                return False
    return True
    
def main():
    flowers = int(input())
    table = []
    for rows in range(flowers):
        column = input().split()
        for x in range(flowers):
            column[x] = int(column[x])
        table.append(column)
    rotation = []
    
    correct = Check(table, flowers)
    while not correct:
        table = Rotate(rotation, table, flowers)
        correct = Check(table, flowers)
    
    for x in range(flowers):
        for y in range(flowers):
            print(table[x][y],end=" ")
        print()
main()
