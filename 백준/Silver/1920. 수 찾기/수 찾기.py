# 입력
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

# 이진 탐색이니까 sort는 필수고,
A.sort()

for i in B: # B안에 있는 원소들이 A에 있으면 1프린트, 브레이크
    first, last = 0, N-1 # 인덱스
    isExist = False # 찾음 여부
    
    # 원소별로 이분탐색
    while first <= last: # first값이 계속 위로가다가 끝값과 같아져버리면.
        mid = ( first + last ) // 2 # 반으로 나눴을 때의 몫 / 아래서 올리고 내린 것들이 여기에 반영
        if i == A[mid]:
            isExist = True
            print(1)
            break
        elif i > A[mid]:
            first = mid + 1 ## 첫번째 값이었던 0을 미드보다 1 올림.
        else:
            last = mid - 1 ## 마지막 값을 미드보다 1 낮춤.
    
    if not isExist: # 찾지 못한 경우
        print(0)    # 0 출력
