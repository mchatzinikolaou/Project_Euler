n=1
for i in range(2,100):
    n=n*i

print(n)
print(sum(int(x) for x in list(str(n))))