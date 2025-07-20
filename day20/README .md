## 📘 문제 이름
    음양 더하기

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

---

### 🧠 문제 설명

어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return
---

### 💡 아이디어

zip(absolutes, signs)
→ 두 리스트를 짝지어 순서대로 묶음. 예: [(4, True), (7, False), (12, True)]

val if sign else -val
→ sign이 True면 양수, False면 음수로 처리.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

zip()을 이용하면 여러 리스트를 순서대로 묶어서 처리할 수 있다는 점.


---

### 다른 사람의 풀이

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))