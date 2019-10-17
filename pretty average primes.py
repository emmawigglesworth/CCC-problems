def Primes():
    prime = []
    for x in range(2,20001):
        count = 0
        for y in range(2,20001):
            if (x%y) == 0:
                count += 1
            if count > 1:
                break
        if count == 1:
            prime.append(x)
    return prime

def Solve(number, primelist):
    primesum = number*2
    for x in range(len(primelist)):
        first=primelist[x]
        for y in range(len(primelist)):
            second=primelist[y]

            if first+second == primesum:
                answer = [first, second]
                return answer
            
def CollectAnswers(cases, nums, primelist):
    answerlist = []
    for x in range(cases):
        number = nums[x]
        answer = Solve(number, primelist)
        answerlist.append(answer)
    return answerlist

def PrintAnswer(cases, answerlist):
    for x in range(cases):
        for y in range(2):
            print(str(answerlist[x][y]),end=" ")
        print()
    
def main():
    cases = int(input())
    nums = []
    for x in range(cases):
        nums.append(int(input()))
    primelist = Primes()
    answerlist = CollectAnswers(cases, nums, primelist)
    PrintAnswer(cases, answerlist)

main()
