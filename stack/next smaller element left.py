arr=[1,3,2,4]
a1=[]
l=[]
for i in range(len(arr)):
    while (len(a1)>0) and a1[-1]>=arr[i]:
        a1.pop()
    if len(a1)==0:
        l.append(-1)
    else:
        l.append(a1[-1]) 
    a1.append(arr[i])

print(l)