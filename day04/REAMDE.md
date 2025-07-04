## 📘 문제 이름
   자연수 뒤집어 배열로 만들기

- 🧩 난이도: 초중급 level1
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12932)

---

### 🧠 문제 설명
    자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

---

### 💡 아이디어
   int(digit) for digit in str(n) - 문자를 정수호 변환해 리스트로 나열
--- 

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

     [::-1] - 리스트를 뒤집는 슬라이싱 문법이다

---

### 다른 사람의 풀이

def digit_reverse(n):
    return list(map(int, reversed(str(n))))
