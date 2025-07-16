## 📘 문제 이름
두 정수 사이의 합

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬 
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12912)

---

### 🧠 문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수

---

### 💡 아이디어
min(a, b)는 두 수 중 더 작은 값

max(a, b)는 두 수 중 더 큰 값

range(min, max + 1)은 작은 수부터 큰 수까지 포함한 숫자들의 리스트

sum(...)은 그 숫자들의 총합을 계산

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
range(start, end + 1) 형태로 사용하면 끝 값까지 포함한 범위까지 이용가능

---

### 다른 사람의 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

