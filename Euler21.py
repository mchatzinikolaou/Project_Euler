import math
divisorList= {}
for num in range(2,10000+1):
    divisors=[]
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            divisors.append(i)
            if i**2!=num:
                divisors.append(num//i)
    # +1 because we skipped division
    # with 1 since it also adds n itself
    divisorList[num]=sum(divisors)+1


amicableNumbers=[]
for i in divisorList.keys():
    if i not in amicableNumbers:
        if divisorList[i] in divisorList.keys():
                                                  #no such thing as
                                                  #a self-amicable
                                                  #number
            if divisorList[divisorList[i]]==i and i!=divisorList[i]:
                amicableNumbers.append(i)
                amicableNumbers.append(divisorList[i])

print(sum(amicableNumbers))