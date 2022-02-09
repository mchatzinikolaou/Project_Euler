def value(string):
    value=0
    for i in range(len(string)):
        value+=ord(string[i])-ord('A')+1
    return value


with open("./p022_names.txt","r") as file:
    words=file.readline().split(",")
    namelist=[]
    for word in words:
        namelist.append(word.strip("\""))
    file.close()
namelist=sorted(namelist)
score=0
for i in range(len(namelist)):
    score+=(i+1)*value(namelist[i])
print(score)