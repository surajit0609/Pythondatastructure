a=[4,2,1,5,6,3,2,4,2]
ps=[]
s1=[]
ns=[]
s2=[]
for i in range(len(a)):
    while len(s1)!=0 and a[s1[-1]]>=a[i]:
        s1.pop()
    if len(s1)==0:
        ps.append(-1)
    else:
        ps.append(s1[-1])
    s1.append(i)
print(ps)
for  j in range (len(a))
