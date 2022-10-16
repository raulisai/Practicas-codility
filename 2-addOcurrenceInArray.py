
def solution(A):
    N=len(A)
    arr=[]

    if not A:
        return arr

    for i in range(N):
        PosFind=A[i] in arr
        if PosFind:
            arr.remove(A[i])
            print('SE elimino ', A[i])
        else:
            arr.append(A[i])
            print('SE agrego ', A[i])

    resul=arr[0]
    return resul  
    pass


print(solution([9,3,9,3,9,7,9]))