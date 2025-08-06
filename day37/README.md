## 📘 문제 이름
문자열 다루기 기본

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12918)

---

### 🧠 문제 설명

문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
---

### 💡 아이디어

len(s) == 4 or len(s) == 6
→ 길이가 4 또는 6인지 확인

s.isdigit()
→ 문자열이 숫자로만 이루어졌는지 확인하는 문자열 메서드
(공백, 기호, 문자 포함 시 False)

and로 두 조건을 모두 만족해야만 True 반환


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

str.isdigit() 메서드를 활용하면 문자열이 숫자인지 간단히 검사할 수 있음

---

### 다른 사람의 풀이

def alpha_string46(s):
    #함수를 완성하세요

    return s.isdigit() and len(s) in [4,6]
