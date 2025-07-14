## 📘 문제 이름
   문자열을 정수로 바꾸기 

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12925)

---

### 🧠 문제 설명
 
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
---

### 💡 아이디어

int() 함수는 문자열을 정수로 자동 변환

문자열 s에는 +나 - 부호가 포함될 수 있기 때문에, int()는 이를 올바르게 처리

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)


---

### 다른 사람의 풀이
def strToInt(str):
    return int(str)

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("51"));