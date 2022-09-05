arr=[100,80,60,70,60,75,85,60,200]
s1=[]
l=[]
l.append(1)
s1.append(0)
for i in range(1,len(arr)):
    while len(s1)>0 and arr[s1[-1]]<=arr[i]:
        s1.pop()
    if len(s1)==0:
        l.append(i+1)
    else:
        l.append(i - s1[-1])
    s1.append(i)
print(l)