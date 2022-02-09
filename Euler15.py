#It's (n by n/2) combinatorics since it's all a question
#of "how many times will i go down?". 1 means go down, 0
# go right, we must always go half of the times to the right,
# and the other half downwards. So (n by n/2)
# = 1*...n / 1...n/2 * 1...n/2 = (n/2)+1 ... n / 1...n/2
denom=1
nom=1
for i in range(1,21):
    denom=denom*i
for i in range(21,41):
    nom=nom*i

print(nom//denom)