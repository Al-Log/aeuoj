## 📘 문제 이름
부족한 금액 계산하기

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/82612)

---

### 🧠 문제 설명

새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.

---

### 💡 아이디어

price + 2*price + 3*price + ... + count*price
= price * (1 + 2 + 3 + ... + count)
= price * count * (count + 1) // 2

total - money: 실제 필요한 금액에서 가진 돈을 뺌

max(0, ...): 모자라는 금액이 음수일 경우 0으로 보정


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

max() 함수를 통해 음수 결과 방지 처리

---

### 다른 사람의 풀이

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
