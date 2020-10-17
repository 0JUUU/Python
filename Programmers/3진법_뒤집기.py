def solution(n):
    answer = 0
    three = []
    while n != 0:
        three.append(n % 3)
        n = n // 3

    cnt = 1
    for i in reversed(three):
        answer += i * cnt
        cnt *= 3
        
    return answer