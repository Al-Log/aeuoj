## 📘 문제 이름
x만큼 간격이 있는 n개의 숫자


- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12954)

---

### 🧠 문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

### 💡 아이디어

range(1, n+1)은 1부터 n까지의 숫자 생성

각 숫자에 x를 곱해서 리스트로 반환

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)



### 다른 사람의 풀이
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))