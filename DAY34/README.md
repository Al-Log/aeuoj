## 📘 문제 이름

약수의 갯수와 덧셈

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/77884)

---

### 🧠 문제 설명

두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

---

### 💡 아이디어

약수의 개수가 홀수인 수 = 완전제곱수

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

제곱수 판별은 sqrt(n).is_integer()로 간단하게 처리할 수 있음



---

### 다른 사람의 풀이

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
