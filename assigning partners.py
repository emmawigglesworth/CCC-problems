def test(first, second, nameNum):
    for x in range(nameNum):
        partner = second[x]
        for y in range(x+1,nameNum-1):
            if first[y]==(partner):
                index = y
                if second[index]!= first[x]:
                    return False
    return True

def main():

    nameNum = int(input())
    first = input()
    first = first.split()
    second = input()
    second = second.split()

    result = test(first, second, nameNum)

    if result:
        print("good")
    else:
        print("bad")

main()
