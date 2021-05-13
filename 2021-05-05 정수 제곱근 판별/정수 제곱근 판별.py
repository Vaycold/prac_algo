from math import sqrt
def solution(n):
    return -1 if round(sqrt(n)) != sqrt(n) else (sqrt(n)+1)**2
