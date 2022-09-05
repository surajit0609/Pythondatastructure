# lis=[10,20,30,'+','*']
# [10,20,30,'+','*']
# list2=[]
lis=[4,3,5,2,'+','*','+']
lis1=[]
for i in lis:
    if i in ['*','+','-']:
        # list2.append()
        a=lis1.pop()
        b=lis1.pop()
        c=0
        if i=='*':
            c=a*b
        elif i=='+':
            c=a+b
        elif i=='-':
            c=a-b
        lis1.append(c)
        
    else:
        lis1.append(i)        
print(lis1)

