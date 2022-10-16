
def solution(A,K):
    N=len(A)
    arr=[]
    print(K,N)
    if not A or K==0:
        return A
    K= K % N        
    for i in range(N):
        #0-2+0=2 START IN POSITION 2 5-1=0
        posNew=(N-K+i)%N
        print(posNew)
        arr.append(A[posNew])
        print()
    
    return arr    
    pass


print(solution([2,0,9,8,6], 6))