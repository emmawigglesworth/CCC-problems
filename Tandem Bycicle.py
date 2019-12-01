#Tandem Bicycle 02/08/19

def FirstQuestion(citizens,dmojlist,peglist):
    total = 0
    for x in range(citizens):
        faster = dmojlist[x]
        slower = peglist[x]
        if slower > faster:
            temp = slower
            faster = slower
            faster = temp
        speed = faster
        total = total + int(speed)
    return total

def SecondQuestion(citizens,dmojlist,peglist):
    total = 0
    for x in range(citizens):
        faster = dmojlist[citizens-1-x]
        slower = peglist[x]
        if slower > faster:
            temp = slower
            faster = slower
            faster = temp
        speed = faster
        total = total + int(speed)
    return total

def main():
    question = int(input())
    citizens = int(input())

    dmolist = input().split()
    for x in range(len(dmolist)):
        dmolist[x] = int(dmolist[x])
    dmolist.sort()

    peglist = input().split()
    for x in range(len(dmolist)):
        peglist[x] = int(peglist[x])
    peglist.sort()
    if question == 1:
        total = FirstQuestion(citizens,dmolist,peglist)
    else:
        total = SecondQuestion(citizens,dmolist,peglist)
    print(total)
main()
