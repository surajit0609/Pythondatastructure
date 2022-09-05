arr=[4,5,6,7]
s1=[]
l=[]
for i in range (len(arr)):
    while len(s1)!=0 and s1[-1]>=arr[i]:
        s1.pop()
    else:
        s1.append(arr[i])
print(s1[0])