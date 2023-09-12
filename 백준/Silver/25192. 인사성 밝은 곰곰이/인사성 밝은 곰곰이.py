# 리스트로 접근하면 시간초과가 발생 -> 딕셔너리로 접근하면 감축

first = int(input()) # 첫째줄 채팅방의 기록수
# map함수(객체)는 for문에 넣을 수 없다.
cnt = 0
# 리스트를 두개 만들어 주는게 나을듯 <- 그래야 중복 이름 나올 때를 구분지을 수 있음.
dic = {}

for i in range(first):
    inputs = input()

    if inputs == "ENTER":
        #for key,value in dic.items():
        #    if value == 1: # value가 1이라는 거는 닉네임마다 하나의 밸류로 주기 위함
        #        cnt += 1
        dic = {}
    else:
        if inputs not in dic: # 키값이 딕셔너리에 없으면
            dic[inputs] = 1
            cnt += 1
print(cnt)