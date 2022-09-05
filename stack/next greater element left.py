arr=[1,3,2,4]
s1=[]
l=[]
for i in range (len(arr)):
    while len(s1)>0 and s1[-1]<=arr[i]:
        s1.pop()
    if len(s1)==0:
        l.append(-1)
    else:
        l.append(s1[-1])
    s1.append(arr[i])
print(l)