## 📘 문제 이름
나누어 떨어지는 숫자 배열


- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12910)

---

### 🧠 문제 설명

array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수

---

### 💡 아이디어

[num for num in array if num % divisor == 0]
→ divisor로 나누어 떨어지는 숫자만 걸러냄
(즉, 나머지가 0인 값만 추림)

sorted(result)
→ 결과 배열을 오름차순 정렬

if result else [-1]
→ 나누어 떨어지는 값이 없다면 [-1] 반환
---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)


---

### 다른 사람의 풀이

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]