dic={
    1: "one",
    2: "two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    15:"fifteen",
    18:"eighteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
}


def toString(num):
    if num in range(1,13):
        return dic[num]
    elif num in range(13,20):
        return (str(dic[num-10])+"teen") if num not in dic.keys() else (dic[num])

    elif num in range(20,100):
        decs=num//10
        units=num%10
        return dic[decs*10] if units==0 else dic[decs*10]+"-"+dic[units]

    elif num in range(100,1000):
        hundreds=num//100
        decs=(num%100)//10
        units=(num%10)
        return dic[hundreds]+" hundred" if num%100==0 else dic[hundreds]+" hundred and "+toString(decs*10+units)
    elif num == 1000:
        return "one thousand"

superstring=""
for  i in range(1,1001):
    superstring+=toString(i)
superstring=superstring.replace(" ","")
print(len(superstring))