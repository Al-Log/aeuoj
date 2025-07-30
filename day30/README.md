## 📘 문제 이름

가운데 글자 가져오기


- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12903)

---

### 🧠 문제 설명

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

---

### 💡 아이디어

len(s) → 문자열의 길이를 구함

mid = length // 2 → 가운데 인덱스 계산

길이가 짝수면 s[mid-1:mid+1] 슬라이싱

길이가 홀수면 s[mid] 한 글자만 반환


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)


---

### 다른 사람의 풀이
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]


print(string_middle("power"))