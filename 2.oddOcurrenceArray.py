

from operator import le


def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    for i in range(0,len(A)-1,2):
        if A[i+1] != A[i]:
            return A[i]  
    return A[-1]
    pass



print(solution([9,3,9,3,9,7,9]))