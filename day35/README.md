## 📘 문제 이름
문자열 내림차순으로 배치하기

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12917)

---

### 🧠 문제 설명

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

---

### 💡 아이디어

sorted(s) : 문자열을 문자 단위로 정렬 (기본은 오름차순)

reverse=True : 내림차순으로 정렬

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

파이썬의 정렬은 유니코드 순서

---

### 다른 사람의 풀이

def solution(s):
    s = list(s)
    s.sort(reverse = True)
    answer = ""
    for i in s:
        answer = answer + i
    return answer
