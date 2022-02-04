num=2*3*5*7*11*13*17*19
j=1

while(
       num%2!=0       or num%3!=0
    or num%4!=0       or num%5!=0
    or num%6!=0       or num%7!=0
    or num%8!=0       or num%9!=0
    or num%10!=0      or num%11!=0
    or num%12!=0      or num%13!=0
    or num%14!=0      or num%15!=0
    or num%16!=0      or num%17!=0
    or num%18!=0      or num%19!=0
    or num%20!=0
    ):
    j=j+1
    num=num*j

print(num,j)