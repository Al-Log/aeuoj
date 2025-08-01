## 📘 문제 이름
  내적

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/70128)

---

### 🧠 문제 설명

길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.


---

### 💡 아이디어
zip(a, b) : 배열 a와 b의 같은 인덱스 요소들을 묶어줌 → (a[0], b[0]), (a[1], b[1]), ...

x * y for x, y in zip(a, b) : 각각 곱함

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

zip()과 리스트 컴프리헨션, sum()의 조합으로 수학적인 연산을 간단하게 구현할 수 있다는 점.

---

### 다른 사람의 풀이


solution = lambda x, y: sum(a*b for a, b in zip(x, y))

