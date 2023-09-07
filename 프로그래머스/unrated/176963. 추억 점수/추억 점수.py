def solution(name, yearning, photo):
    # 사람들의 이름들이 담긴 name, 사람별 점수를 담은 정수 배열, 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어짐.
    
    # name, yearning은 매칭 되어 있고, photo 요소 하나하나에 매칭해서 점수 리턴
    
    photo_indexes = [] # 인덱스모음
    straight_result = [0]*len(photo)
    
    dic_name = {v:i for i,v in enumerate(name)} # 이 이름 안에 없으면 0점 
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in dic_name.keys():
                photo_indexes.append(dic_name[photo[i][j]]) # 딕셔너리[키] => 값
                # 인덱스 넣고, 이 인덱스를 바로 yearning에 대입하고 싶은데
                straight_result[i] += yearning[dic_name[photo[i][j]]]
    
    return straight_result