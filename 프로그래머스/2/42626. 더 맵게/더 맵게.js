// 힙 자료구조로 풀어야 함..
// 최소 힙에서는 부모 노드가 작은 값이고, 부모 노드 아래에 자식 노드 두개, 루트 노드가 최상위 부모 노드

class Heap {
  constructor() {
    this.items = []; // 힙 요소들을 배열에 저장
  }

// 자리 바꾸기 함수
  swap(index1, index2) {
    [this.items[index1], this.items[index2]] = [
      this.items[index2],
      this.items[index1],
    ];
  }
    
// 삽입 함수
  insert(val) {
    this.items.push(val); // 값을 배열의 끝에 추가
    let index = this.items.length - 1; // 끝에 추가한 요소의 인덱스*
    while (true) { // *최소 힙 조건이 만족될 때까지 반복
        // - 추가한 녀석이 부모 노드랑 비교하면서 부모 노드보다 작을 경우 자리를 교체해나가는 로직
      
        let parentIndex = Math.floor((index - 1) / 2); // 부모 인덱스 계산
      
        // 부모보다 자식이 작으면 자리 바꾸기
        if (this.items[index] < this.items[parentIndex]) {
            this.swap(index, parentIndex);
          } else break;
          index = parentIndex; // 부모 인덱스로 이동
          if (index < 1) break; // 루트 노드(=0)에 도달하면 종료
        }
      }
    
    // 최소값 제거 함수 - *힙의 특성을 유지하기 위한 로직 : 루트 노드를 제거하면 힙의 조건이 위배되기에 마지막 요소를 루트로 이동시키고, 그 위치에서부터 다시 힙의 조건을 만족하도록 재구성 -> 이 과정을 통해 루트 노드를 제거하면서 힙의 조건을 유지할 수 있다.
    // 마지막 요소를 제거하는 이유는 힙은 완전 이진 트리 형태를 유지해야 하는데, 완전 이진 트리에서
    // 마지막 레벨은 왼쪽부터 채워져 있어야 한다. 따라서 마지막 요소를 루트 위치로 이동시킨 후에는 그 위치에는 원래 루트 노드의 값이 있어야 하고, 마지막 요소는 제거되어야 한다. 이렇게 힙의 특성을 유지하면서 요소를 추가하고 제거해야 함.
  removeMin() {
    this.items[0] = this.items[this.items.length - 1]; // 마지막 요소를 루트로 이동
    this.items.pop(); // 루트노드(마지막 요소의 값을 가진) 제거
    if (this.items.length <= 1) return; // 힙 크기가 1 이하면 종료
 
    let index = 0;
    while (true) {
      //  두 자식중 작은값의 자식 인덱스 찾기 - 가장 작은 값을 찾아서 루트로 이동시키는 로직
      let lChildIndex = index * 2 + 1;
      let rChildIndex = index * 2 + 2;
      let minIndex = index;
      if (
        lChildIndex < this.items.length &&
        this.items[minIndex] > this.items[lChildIndex]
      ) {
        minIndex = lChildIndex;
      }
      if (
        rChildIndex < this.items.length &&
        this.items[minIndex] > this.items[rChildIndex]
      ) {
        minIndex = rChildIndex;
      }
      //  위치 바꾸기
      if (minIndex !== index) {
        this.swap(index, minIndex);
        index = minIndex;
      } else break; // 최소 힙 조건이 만족될 때까지 반복
    }
  }
}

function solution(scoville, K) {
  let answer = 0;

  //  힙생성과 scoville 힙에 저장
  let scovilleHeap = new Heap();
  scoville.forEach((el) => {
    scovilleHeap.insert(el);
  });

  //  스코빌 지수 설정
  while (true) {
    if (scovilleHeap.items[0] >= K) break;
    if (scovilleHeap.items.length <= 1) {
      answer = -1; // 모든 음식의 스코빌 지수를 K이상으로 만들 수 없으면 -1 리턴
      break;
    }    
    // 첫번째 녀석들을 두개(최소, 두번째로 작은) 제거하고, 그 두 녀석의 스코빌 지수가 K이상이면 종료 
    const low1 = scovilleHeap.items[0];
    scovilleHeap.removeMin();
    const low2 = scovilleHeap.items[0];
    scovilleHeap.removeMin();
    scovilleHeap.insert(low1 + low2 * 2);

    answer++;
  }

  return answer;
}

// function solution(scoville, K) {
//     var answer = 0;
    
//     // 로직
//     // 0. 모든 음식의 스코빌 지수가 K이상이 될 때까지 반복
//     // 1. 모든 음식의 스코빌 지수는 k이상으로 만들려면 낮은 수 두개를 섞어서 7이상으로 만들어야 함
//     // 2. 그 횟수의 최소 값을 리턴
    
// //     scoville.sort((a,b) => b-a); // 배열을 오름차순으로 정렬
    
// //     const minValue = Math.min(...scoville); // 배열에서 최소값을 구하려면 spread 연산자 ...
// //     const second_minValue = scoville[1];
    
// //     for (i = 1; minValue < K; i++) {
// //         mixed_sco = minValue + (second_minValue * 2)
// //         // 배열에 앞에 추가하고, 그 전에 미니멈 두개 삭제하고
// //         scoville.splice(0,2); // 인덱스 0부터 2개의 요소 차례로 삭제 - 인덱스로 접근할거면, sorted 계속 해야 함.
// //         scoville.push(mixed_sco);
// //         scoville.sort((a,b) => a-b); // 다시 오름차순으로

// //         answer = i;
// //     }
    
//     return answer;
// }