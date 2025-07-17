def solution(s):
    s = s.lower()  # 대소문자 구별 없이 비교하기 위해 모두 소문자로 변환
    return s.count('p') == s.count('y')
print(solution("pPoooyY"))  # True (p:2, y:2),예시코드