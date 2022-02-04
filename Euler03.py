num=600851475143 

results=[]


def koskino(num):

    factor=2
    while (factor<=num):
        dividant,modulo=divmod(num,factor)
        if(modulo ==0):
            return factor,dividant
        factor+=1
    return factor,1


while(koskino(num)[1]!=1):
    result=koskino(num)
    results.append(result[0])
    num=result[1]

results.append(num)
print(max(results))
