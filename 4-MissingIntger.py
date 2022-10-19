
def solution(A):
    N=len(A)
    arr=dict()
    Nmin=A[0]


    for i in range(N):
        if A[i]< Nmin:
            arr[A[i]]=False
            if  (A[i]+1) not in arr:
                arr[A[i]]=True
                Nmin=A[i]
            else:
                if (Nmin+1) == A[i]:
                    arr[Nmin]=False
                    Nmin=max(arr)
        else:
            if (Nmin+1) == A[i]:
                arr[A[i]]=False
                arr[Nmin]=False
                Nmin=max(arr)
            else:
                arr[A[i]]=False
                Nmin=max(arr)
            
    for i in range(len(arr)):
        if arr.get(i)==True:
            resul=list(arr.keys())
            resul1=i+1
            
            return resul1
    return 1
    pass


print(solution([ 3, 6,1,5,2 ]))