# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    N=bin(N)[2:]
    print("Numne binario: ",N)
    maxGap=0
    maxb=0
    for k in N:
        print("k",k)
        if int(k)==0:
                maxb+=1
                print("maxb- entre en el if",maxb)
        elif int(k)==1:
                maxGap=max(maxGap,maxb) 
                print("maxGap- entre enm el else",maxGap)
                maxb=0

    return maxGap    

resul = solution(200)

print(resul)