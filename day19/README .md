## 📘 문제 이름
하샤드 수 

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12947)

---

### 🧠 문제 설명

문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수
---

### 💡 아이디어

str(x)
→ 숫자 x를 문자열로 변환해서 자릿수 하나하나 접근할 수 있게 함.

int(digit) for digit in str(x)
→ 각 자릿수를 정수형으로 바꿔 리스트로 생성.

sum(...)
→ 자릿수의 합을 계산.

x % digit_sum == 0
→ 자릿수의 합으로 나누어 떨어지는지 확인.
---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

sum()과 리스트 컴프리헨션을 함께 쓰면 자릿수 합 계산을 한 줄로 간결하게 처리할 수 있다는 점.

---

### 다른 사람의 풀이
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

 # 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
