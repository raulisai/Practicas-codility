

from xml.dom.minidom import Element


def solution(A):
    NumberThatExist=set()
    for i in range(len(A)):
        if A[i] >0:
            NumberThatExist.add(A[i])
    if len(NumberThatExist)==0:
        return 1
    for i in range(1,len(A)+1):
        if i not in NumberThatExist:
            return i
        if i == len(A):
            return i+1
    
    return 0

    pass



print(solution([1, 3, 6, 4, 1, 2]))