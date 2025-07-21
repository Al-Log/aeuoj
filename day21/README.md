## 📘 문제 이름
     없는 숫자 더하기

- 🧩 난이도:초중급 
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/86051)

---

### 🧠 문제 설명

   0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다
   numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return

---

### 💡 아이디어

set(numbers)는 주어진 배열의 숫자를 집합으로 변환

set(range(10)) - set(numbers)는 0~9 중 numbers에 없는 숫자들 찾기
---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

차집합(-) 연산을 통해 어떤 값이 누락되었는지 쉽게 찾을 수 있다는 걸 배울 수 있었음

---

### 다른 사람의 풀이

def solution(numbers):
    return 45 - sum(numbers)