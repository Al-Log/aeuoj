def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        # 약수의 개수가 홀수인 경우는 제곱수일 때만 발생함!
        if (num ** 0.5).is_integer():
            answer -= num  # 홀수 개 → 빼기
        else:
            answer += num  # 짝수 개 → 더하기
    return answer