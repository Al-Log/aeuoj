## 📘 문제 이름
 
제일 작은 수 제거하기

- 🧩 난이도: 초중급
- 🛠 사용 언어: 파이썬
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12935)

---

### 🧠 문제 설명

정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요

---

### 💡 아이디어

len(arr) == 1
→ 요소가 하나뿐이라면 제거 후 빈 배열이 되므로 [-1]을 리턴

min(arr)
→ 배열에서 가장 작은 값을 찾음

arr.remove(min_val)
→ 가장 작은 값을 배열에서 제거 (처음 등장한 하나만 제거)

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)


---

### 다른 사람의 풀이

def rm_small(mylist):
    # 함수를 완성하세요
    return [i for i in mylist if i > min(mylist)]

my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
