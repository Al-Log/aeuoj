def solution(x):
    digit_sum = sum(int(digit) for digit in str(x))  # 자릿수 합
    return x % digit_sum == 0