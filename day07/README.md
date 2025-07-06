## 📘 문제 이름
     평균구하기

- 🧩 난이도:초중급 
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12944)

---

### 🧠 문제 설명
    정수를 담고 있는 배열 arr의 평균값을 return하는 함수,

---

### 💡 아이디어
    sum(arr)-리스트 arr 안에 있는 모든 정수의 합계를 구하는 내장 함수
    len(arr)-리스트 arr의 개수를 구해요.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)


---

### 다른 사람의 풀이
def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    return sum(list) / len(list)
