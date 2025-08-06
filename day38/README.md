## 📘 문제 이름
행렬의 덧셈

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12950)

---

### 🧠 문제 설명

행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

---

### 💡 아이디어

zip(arr1, arr2)
→ 두 행렬의 행들을 각각 묶음

zip(row1, row2)
→ 각 행의 원소들을 묶어서 같은 위치끼리 더함

[a + b for a, b in zip(...)]
→ 각 원소를 더해서 새 행 생성

전체는 중첩 리스트 컴프리헨션으로 2차원 배열 형태 반환


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)


---

### 다른 사람의 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer
