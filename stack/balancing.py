## Q1:-Discuss how stack can be used for checking balancing of symbols ?
def stack_balancing(exp):
    stack=[]
    for char in exp:
        if char in ['(','{','[']:
            stack.append(char) 
        else:
            if len(stack)==0:
                return False
            elif len(exp)%2!=0:
                return False
            elif (stack[-1]=='(' and char == ')') or (stack[-1]=='{' and char == '}') or (stack[-1]=='[' and char == ']') :
                 stack.pop()
            else:
                return False
    if len(stack)==0:
        # print("balance")
        return True
    else:
        # print("not balance")
        return False
__name__ == "__main__"
exp='({[])}'

if stack_balancing(exp):
    print('balanc')
else:
    print("not banance")




    

        

           
    
            
            
            
