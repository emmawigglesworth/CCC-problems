
def Largest(readings):
    largest = 0
    for x in range(len(readings)):
        if readings.count(readings[x]) > readings.count(readings[largest]):
            largest = x
        elif readings.count(readings[x]) == readings.count(readings[largest]):
            if readings[x]>readings[largest]:
                largest = x
    return largest

def Duplicate(readings, largest):
    for x in range(len(readings)):
        if readings[x] != readings[largest]:
            if readings.count(readings[x]) == readings.count(readings[largest]):
                return True
    return False

def SecondLargest(readings,largest):
    for x in range(len(readings)):
        if readings.count(readings[x]) < readings.count(readings[largest]):
            second = x
            
    for x in range(len(readings)):
        if readings[x] != readings[largest]:
            if readings.count(readings[x]) > readings.count(readings[second]):
                second = x
            elif readings.count(readings[x]) == readings.count(readings[second]):
                if readings[x] > readings[second]:
                    second = x
    return second
                    
def BiggestDiff(readings,largest):
    for x in range(len(readings)):
        if readings[x] != readings[largest]:
            if readings.count(readings[x]) == readings.count(readings[largest]):
                pos = x
    for x in range(len(readings)):
        if readings[x] != readings[largest]:
            if readings.count(readings[x]) == readings.count(readings[largest]):
                if readings[largest] > readings[x]:
                    if readings[largest] - readings[x] > readings[largest] - readings[pos]:
                        pos = x
                else:
                    if readings[x] - readings[largest] > readings[pos] - readings[largest]:
                        pos = x
    return pos

def SecondBiggestDiff(readings,second,largest):
    for x in range(len(readings)):
            if readings.count(readings[x]) == readings.count(readings[second]):
                    pos = x
    for x in range(len(readings)):
            if readings.count(readings[x]) == readings.count(readings[second]):
                if readings[largest] > readings[x]:
                    if readings[largest] - readings[x] > readings[largest] - readings[pos]:
                        pos = x
                else:
                    if readings[x] - readings[largest] > readings[pos] - readings[largest]:
                        pos = x
    return pos
def main():
    sensors = int(input())
    readings = []
    for x in range(sensors):
        current = int(input())
        readings.append(current)
        
    largepos = Largest(readings)
    if Duplicate(readings,largepos):
        secondpos = BiggestDiff(readings,largepos)
    else:
        secondpos = SecondLargest(readings,largepos)
        if Duplicate(readings,secondpos):
            secondpos = SecondBiggestDiff(readings,secondpos,largepos)
    largest = readings[largepos]
    second = readings[secondpos]

    if largest > second:
        difference = largest-second
    else:
        difference = second-largest
    print(difference)
main()

