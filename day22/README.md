## 📘 문제 이름

정수 내림차순으로 배치하기

- 🧩 난이도: 초중급
- 🛠 사용 언어:파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

---

### 🧠 문제 설명

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴
---

### 💡 아이디어

1.sorted(..., reverse=True) 문자열의 각 자릿수를 내림차순으로 정렬

2.''.join(...) 정렬된 숫자들을 다시 하나의 문자열로 붙이기

3.int(...) 문자열을 정수로 변환해서 최종 결과로 반환



---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

숫자이지만 자릿수 기준으로 조작할 때는 문자열로 변환하는 게 훨씬 유리함.


---

### 다른 사람의 풀이

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))