def solution(n):
    f = []
    f.append(0)
    f.append(1)
    for i in range(1,n+1):
        f.append(f[i-1]+f[i])# f[n+1]까지 만드는 것
    answer = f[n]%1234567
    return answer