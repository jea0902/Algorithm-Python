def solution(s):
    
    # 일단 공백을 기준으로 split을 해서 리스트로 만들고, - 공백이 하나 이상이네
    a = s.split(" ")
    # 이러면 공백이 몇개 이상이더라도 문자들은 문자대로, 공백들은 공백으로 스플릿
    # 조건문으로 문자가 있는 애들만 인덱스별로 바꿔주고
    
    new_list = [] # 결과를 담을(문자열은 바꿀 수가 없어서 새로 만듦)
    
    # 문자열은 불변(immutable)한 객체라서 문자열의 특정 위치의 문자를 직접 변경할 수 없다..
    
    for i in a:
        if i != "":
            new_word = ""
            for j in range(0,len(i)):
                if j%2 == 0:
                    new_word += i[j].upper()
                else:
                    new_word += i[j].lower()
            new_list.append(new_word)
        else:
            new_list.append(i)
            
    answer = " ".join(new_list) # join도 원본값에 변화는 없네
    return answer