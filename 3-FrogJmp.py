def solution(X,Y,D):
    v = (Y-X)//D
    print(v)
    if X+v*D >= Y:
        return v
    else:
        return v+1
    pass



print(solution(10,85,30))