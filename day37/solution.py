def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

print(solution("1234"))   # 출력: True
print(solution("a234"))   # 출력: False
print(solution("123456")) # 출력: True
print(solution("12345"))  # 출력: False
print(solution("12 34"))  # 출력: False