
from pickle import TRUE


def solution(X, A):
    occupedPosition=dict()
    totalSum=(X*(X+1))/2
    
    for i in range(len(A)):
        if occupedPosition.get(A[i])== None and A[i] <= X:
            occupedPosition[A[i]]=True
            totalSum -= A[i]
            print(totalSum)
            if totalSum == 0:
                return i



    return -1
    pass







print(solution(5,[1,3,6,1,4,2,3,5,4,6,7,8]))
