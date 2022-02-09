divisorSums={}
abundants=[]
N=28123
import math
def createDivisorSums():
    for num in range(2,N):
        divisorSums[num]=1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                divisorSums[num]+=i
                if i!=num//i:
                    divisorSums[num]+=num//i



def findAbundants():
    for num in range(2,N):
        if divisorSums[num]>num:
            abundants.append(num)

def findPerfects():
    for num in range(2,N):
        if divisorSums[num]==num:
            print(num)
def init():
    createDivisorSums()
    findPerfects()
    findAbundants()

init()

print(abundants)

sums=[]
for i in range(len(abundants)):
    print(i)
    for j in range(i,len(abundants)):
        res = abundants[i] + abundants[j]
        if res<=N:
           sums.append(res)


sums=set(sums)
sum=0
for i in range(1,N):
    if i not in sums:
        sum=sum+i
print(sum)
