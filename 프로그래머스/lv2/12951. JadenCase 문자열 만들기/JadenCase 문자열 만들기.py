def solution(s):
    answer = ''
    # 공백문자로도 이어져있으니까
    # split로 잘라내서 리스트 요소마다 첫글자가 문자면 대문자로 바꾸고 아니면 그대로 둬서 합치면 됨
    # **참고로 list(s) 해버리면 문자열 하나하나를 전부 다 잘라서 리스트에 넣어버림
    
    split_s = s.split(" ")
    
    for i in split_s:
        i = i.capitalize()
        if answer == "":
            answer += i
        else:
            answer += " " + i
    
    return answer