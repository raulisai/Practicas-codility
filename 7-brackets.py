
def solution(S):
    S = list(S)
    print(len(S))
    stack = []
    
    for i in range(0,len(S)):
        print("stack",stack,len(stack))
        if S[i] == "(" or S[i] == "[" or S[i] == "{":
            stack.append(S[i])
            print("stack",stack)
        else:
            if len(stack) == 0:
                return 1
            if S[i] == ")" and stack[-1] == "(":
                stack.pop()
                print("stack",stack)
            elif S[i] == "]" and stack[-1] == "[":
                stack.pop()
                print("stack",stack)
            elif S[i] == "}" and stack[-1] == "{":
                stack.pop()
                print("stack",stack)

    if len(stack) == 0:
        return 1
    return 0
    pass    

print( solution("{[()()]}()") )