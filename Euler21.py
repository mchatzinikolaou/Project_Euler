import math
divisorList= {}
for num in range(1,1000+1):
    divisors=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            divisors.append(i)
            if(i**2!=num):
                divisors.append(num//i)

    divisorList[num]=sum(divisors)

print(divisorList)

for divisor in divisorList.keys():
    print(divisor)