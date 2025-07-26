def solution(array, divisor):
    result = [num for num in array if num % divisor == 0]
    return sorted(result) if result else [-1]