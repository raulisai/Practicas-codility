# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    N=bin(N)[2:]
    maxGap=0
    maxb=0
    for k in N:
        if int(k)==0:
                maxb+=1
        elif int(k)==1:
                maxGap=max(maxGap,maxb) 
                maxb=0

    return maxGap    

resul = solution(-34)

print(resul)