arr=[6,4,5,3,2]
s1=[]
l1=[]
for i in range (len(arr)-1,-1,-1):
    while len(s1)>0 and s1[-1]>=arr[i]:
        s1.pop()
    if len(s1)==0:
        l1.append(-1)
    else:
        l1.append(s1[-1])
    s1.append(arr[i])
l1.reverse()
print(l1)