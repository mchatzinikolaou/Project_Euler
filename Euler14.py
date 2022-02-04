numStepDictionary={}

def addToDictionary(dic,num,steps):
    dic[num]=steps


def calcNext(num):
    return  num//2 if  num%2 == 0 else  3*num+1


def getChainLength(init):
    steps=0
    num=init
    while num!=1 and num not in numStepDictionary.keys(): #and num not in the keys of the dictionary
        steps+=1
        num=calcNext(num)

    #if num IN the keys of the dictionary, steps=steps+ value of key
    if num in numStepDictionary.keys():
        steps=steps+numStepDictionary[num]
    #add self to dictionary
    numStepDictionary[init]=steps

for key in range(1,int(1e06)):
   getChainLength(key)


steps=list(numStepDictionary.values())
numbers=list(numStepDictionary.keys())

print(f"number {numbers[steps.index(max(steps))]} with {max(steps)} steps")

def printFullChain(num):
    chain=[]
    num=calcNext(num)
    while(num!=1):
        chain.append(num)
        num=calcNext(num)
    chain.append(1)
    print(chain)
