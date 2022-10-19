
def solution(X,A):
    N=len(A)
    arr=[0]
    WayFull=False
    seg=0
    if not A:
        return arr
    
    while WayFull==False:

        if arr[seg] == X:
            WayFull=True
            seg
        else:
            if arr[seg] > A[seg]:
                arr.append(A[seg])
                arr.sort()
                seg+=1
                print(arr)
            else:
                arr.append(A[seg])
                arr.sort()
                seg+=1
                print(arr)
    return seg 
    pass


print(solution(2,[1,3,1,4,2,3,5,4,6,8]))