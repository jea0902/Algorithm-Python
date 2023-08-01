def solution(code):
    
     # 모드가 제일 앞에 있으면 안됨. code[idx]가 1일 때 바로 모드부터 바꾸어줘야 함.
    
    ret = ""
    mode = 0
    for idx in range(0,len(code)):
        if code[idx] == "1":
            mode += 1
            mode = mode % 2
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                if idx % 2 == 1:
                    ret += code[idx]
    if ret =="":
        ret = "EMPTY"
    return ret