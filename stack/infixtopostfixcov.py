output=[]
operator=[]
priority={'+':1,'-':1,'*':2,'/':2,'(':0}
exp=input("enter the infix value:")
for ch in exp:
    if ch=='(':
        operator.append(ch)
    elif ch==')':
        while operator[-1]!='(':
            em=operator.pop()
            output.append(em)
        operator.pop()
    elif (ch=='*' or ch=='/' or ch=='+' or ch=='-'):
        while len(operator)>0 and priority[operator[-1]]>=priority[ch]:
            em=operator.pop()
            output.append(em)
        operator.append(ch)
    else:
        output.append(ch)
while (len(operator)!=0):
    em=operator.pop()
    output.append(em)
for char in output:
    print(char,end='')





