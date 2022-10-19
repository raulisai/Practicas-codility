def solution(A):
    if len(A)==0:
        return 1
    if len(A) == max(A):
        return max(A)+1
    A.sort()
    find=False
    print(A)
    i=0
    while find==False:
       
        if i+1 != A[i]:
            print("if",i)
            return i+1        
        else:
            i+=1
            print(i)
        

    return i 

    pass

print( solution([2,3,1,5,4,7,6]) ) 