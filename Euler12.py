def getNumberOfDivisors(num):
    divs=2 #one is itself, the other is 1
    for i in range(2,num//2+1):
        if num % i ==0:
            divs+=1
    return divs


triangleNums=[0]

def getNthTriangleNumber(n):
    result=n+triangleNums[n-1]
    triangleNums.append(result)
    return result

i=1
triNum = getNthTriangleNumber(i)
while(getNumberOfDivisors(triNum) <=500):
    i=i+1
    triNum=getNthTriangleNumber(i)

print(triNum)

