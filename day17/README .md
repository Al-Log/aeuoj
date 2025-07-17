## 📘 문제 이름
문자열 내 p와 y의 개수

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12916)

---

### 🧠 문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution함수를 완성
---

### 💡 아이디어
s.lower()
→ 문자열 전체를 소문자로 바꿔서 'P'와 'p', 'Y'와 'y'를 구별하지 않도록 함.

s.count('p')와 s.count('y')
→ 문자열에서 각각의 문자가 몇 번 등장하는지 세어 줌.


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
대소문자 구분 없이 비교할 때는 .lower() 나.upper()를 활용

---

### 다른 사람의 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
