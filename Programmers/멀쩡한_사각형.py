def solution(w,h):
    answer = 1
    answer = int(w) * int(h)
    gcd_v = gcd(int(w), int(h))
    
    answer -= 4 * int(w) // gcd_v
    return answer

def gcd(w,h):
    if w > h :
        a = w
        b = h
    else: 
        a = h
        b = w
    r = -1

    while r != 0:
        r = a % b
        a = b
        b = r

    return a

print(solution(8,12))