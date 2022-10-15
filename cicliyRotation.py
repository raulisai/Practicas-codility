
#[3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#[6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#[7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]



def solution(A, K):
    Num=len(A)
    s1=0
    if int(K) < 100:
        for j in range(K):
            for i in range(Num):
                if i == Num-1:
                    A[0]=s1

                elif i == 0:
                    s1=A[i+1] 
                    A[i+1]=A[i]


                
                else:
                    s2=A[i+1] 
                    A[i+1]=s1
                    s1=s2
    return A

print(solution([3, 8, 9, 7, 6], 0))