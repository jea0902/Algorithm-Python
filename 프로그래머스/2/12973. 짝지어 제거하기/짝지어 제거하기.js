function solution(s)
{
    var answer = 0;
    
    // 반복된 문자열이 있으면 제거
    // 제거된 이후 이어붙임
    // 이어 붙혔을 때도 반복된 경우면 또 제거(앞에서부터 판단)
    
    // 문자열의 길이 제한이 없는 상황이라 효율성 문제 걸릴 거 같다.
    // 자료구조 스택?
    stk= [s[0]];
    s = s.slice(1)
    // while 문으로 바꾼 이유 : for문은 i를 초기화 할 수 없어 그리고 pop으로 삭제할 예정이니까 for문은 오류
    

    for (let i=0; i<s.length; i++){
        first = s[i]
        if (stk[stk.length-1] == first) {
            stk.pop();
        }
        else {
            stk.push(first);
        }
    }
        // while문과
        // first = s[0]
        // s = s.slice(1) // s를 재선언 안하고 for문을 돌리는 건?

    
    if (stk.length === 0) {
        return answer = 1;
    }

    console.log('Hello Javascript')
    return answer;
}