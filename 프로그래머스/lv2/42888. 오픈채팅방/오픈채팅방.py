def solution(record):
    
    userIdandNick = {} # 키를 ID, 값을 닉네임 
    result = []
    
    # 닉네임 변경될 떄는 Enter랑 Change일 떄만
    # 미리 이렇게 만들어 놓는 이유를 물어보기 (원래 아래에서 enter, leave, change일 때 각각 키,값 추가하고, result에 추가하는 방법을 썼었음. - 결국 출력은 한번만 돌아가면 됨. 그래서 닉네임 변경 되는 경우의 수를 미리 빼서 스택처럼 마지막 값에 고정시켜두려고?)
    
    for i in record:
        a = i.split(" ")
        if len(a) == 3:
            userIdandNick[a[1]] = a[2] # 키, 닉네임 고정
    
    # 새로운 리스트 자유롭게 복사해서 사용 (원본 훼손없으면)
    for j in record:
        b = j.split(" ")
        if "Enter" in b:
            result.append("%s님이 들어왔습니다." %userIdandNick[b[1]])
        if "Leave" in b:
            result.append("%s님이 나갔습니다." %userIdandNick[b[1]])
    return result