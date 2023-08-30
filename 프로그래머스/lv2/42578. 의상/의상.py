def solution(clothes):
    
    # clothes의 의상의 종류를 딕셔너리의 key값으로, value를 빈 리스트로 저장
    종류 = {v[1] : [] for v in clothes}
    # {'headgear': [], 'eyewear': []}
    
    # clothes의 값을 하나씩 꺼내며 종류의 value에 추가
    for 옷들 in clothes:
        종류[옷들[1]].append(옷들[0]) # 딕셔[키].append(넣을 값) :  특정 키에다 값을 추가
        
    결과 = 1
    # 딕셔너리 종류의 key값을 꺼내면서 value의 길이 + 1을 no에 곱해줌
    # = 각 의상의 종류의 경우, 입는 경우와 입지 않은 경우가 존재하니까
    # 입지 않은 경우를 추가하여 계산을 해야 됨.
    for key in 종류.keys(): # 종류 하나하나(카테고리)의
        옷개수 = len(종류[key]) # 값의 갯수 - 그 카테고리의 옷 개수
        결과 = 결과 * (옷개수 + 1) 
        
        # headgear = 노란모자, 그린터번, none
        # eyewear = 블루선글라스, none
        # 3 * 2 = 6 
        
    
    return 결과 - 1 # 아무것도 입지 않은 경우의 수 1을 빼줌.
    

    
    
    
    
    
    
    