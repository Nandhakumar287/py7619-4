def createStack():
    stack=[]
    return stack
    
def push(stack,data):
    stack.append(data)
    
def pop(stack): 
    return stack.pop()

str1=input()
stack=createStack()
for i in range(0,len(str1)):
    push(stack,str1[i])
if(stack==stack[-1::-1]):
    print('YES')
else:
    print('NO')
