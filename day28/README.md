## 📘 문제 이름

콜라츠 추측

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12943)

---

### 🧠 문제 설명

주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측


---

### 💡 아이디어

while num != 1
→ 숫자가 1이 될 때까지 작업을 반복합니다.

짝수면 num //= 2, 홀수면 num = num * 3 + 1

매 반복마다 count를 1 증가시킵니다.

500회 이상 반복하면 -1 반환
→ 끝나지 않는 경우를 방지하기 위한 제한입니다.

정상적으로 1이 되면 count를 반환

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

탈출 조건을 명확히 설정하는 것이 중요

---

### 다른 사람의 풀이

def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1