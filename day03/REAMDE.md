## 📘 문제 이름 
      자릿수 더하기


- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12931#)

---

### 🧠 문제 설명

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
---

### 💡 아이디어

sum 함수를 이용해서 각 자릿수를 더하는 방식을 이용


---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

int(digit) for digit in str(n)- 숫자를 한 자리씩 나눠서 각각 다시 정수로 바꾸는 코드


---

### 다른 사람의 풀이
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)

