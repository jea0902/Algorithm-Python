def solution(board, moves):
    answer = 0
    # moves의 크기만큼 움직이고 결과를 뽑아냄.
    
    stacklist=[]
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stacklist.append(board[i][move-1])
                board[i][move-1] = 0 # 빼간 자리를 0으로 만들어줬어야 했네.
                
                if len(stacklist)>1:
                    if stacklist[-1] == stacklist[-2]:
                        # 두개이상 찰 때마다 같은 것끼리 없애줬네.. 스택 문제니까 pop으로
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2 # 터진 인형의 갯수
                break # if문으로 인형을 뽑았으면 더 뽑지 말고 정지
    
    
    
    return answer
    
    
    
    
    
    # 바구니 = [] - 실패 사례
    # for i in moves: # moves 값 하나에
    #     for j in board: # board 원소들 하나하나 0아닌 애 찾고 바구니에 넣고
    #         if j[i-1] != 0:
    #             바구니.append(j[i-1])
    #             continue
    #         else:
    #             continue
    # for k in range(0,len(바구니)-1):
    #     if 바구니[k] == 바구니[k+1]:
    #         바구니[k+1] = 0
    #         answer += 1
    # return answer # 터트려서 사라진 인형의 갯수