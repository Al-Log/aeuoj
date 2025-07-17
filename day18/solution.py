def solution(n):
    x = n**0.5  # n의 제곱근
    if x.is_integer():  # 제곱근이 정수라면
        return int((x + 1) ** 2)
    else:
        return -1
    
print(solution(121))  # 144 (11의 제곱 → (11+1)^2 = 144) /출력예시