numbers=range(999,100,-1)
results=[]

def isPalindrome(number):
    numList=[int(x) for x in str(number)]
    if numList==numList[::-1]:
        return True
    return False

for i in numbers:
    for j in numbers:
        result=i*j
        if (isPalindrome(result)):
            results.append(result)
            break

print(max(results))