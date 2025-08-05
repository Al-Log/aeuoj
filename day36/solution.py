def solution(price, money, count):
    total = price * count * (count + 1) // 2  # 등차수열의 합 공식
    return max(0, total - money)