F1=1
F2=1

i=2
while(len(list(str(F2)))<(1000)):
    i=i+1
    F2=F1+F2
    F1=F2-F1
print(i)