sum=0
last_num=1
num=2

while(num<=4e06):

    if(num%2 == 0 ):
        sum=sum+num

    next_num=num+last_num
    last_num=num
    num=next_num

print(sum)


