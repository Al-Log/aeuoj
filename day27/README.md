## 📘 문제 이름

서울에서 김서방 찾기

- 🧩 난이도: 초중급
- 🛠 사용 언어:파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12919)

---

### 🧠 문제 설명

String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수


---

### 💡 아이디어

seoul.index("Kim")
→ "Kim"이 배열 seoul에서 몇 번째 인덱스에 있는지 찾아줍니다.

f"김서방은 {x}에 있다"
→ f-string을 사용해 문자열 안에 x 값을 자연스럽게 삽입합니다.


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

문자열 포매팅 방법 중 f-string은 가장 간결하고 읽기 쉬운 방식
---

### 다른 사람의 풀이

def findKim(seoul):
    # 함수를 완성하세요

    return "김서방은 {}에 있다".format(seoul.index('Kim'))

