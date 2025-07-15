## 📘 문제 이름
약수의 합

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12928)

---

### 🧠 문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수

---

### 💡 아이디어

range(1, n + 1) → 1부터 n까지 숫자 확인
n % i == 0이면 약수
약수들만 리스트로 만들고 sum()으로 더함

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

약수는 나누어떨어지는 수, 즉 n % i == 0인 i

### 다른 사람의 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])