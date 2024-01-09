def solution(n) :
    
    def _10_to_2(num) :
        ct = 0
        while num != 0 :
            num, div = num // 2, num % 2
            if div == 1 : ct += 1
        return ct
    
    ct = _10_to_2(n)
    while True :
        n += 1
        if _10_to_2(n) == ct : return n
'''
- 10진법의 수를 2진법의 수로 바꾸는 과정에서 1이 나오는 규칙을 이용함.
    - 10진법을 계속 2로 나누면서 나머지가 1일 경우 이진법으로 변환할 때 1이 나옴.
    - 1이 나올 때의 갯수만 세서 `return`
- 처음 주어진 `n` 에 대해  1의 갯수를 먼저 센 후 ( `ct = _10_to_2(n)` )
- 반복하여 1을 더하면서 해당 갯수가 주어진 `n`의 갯수랑 일치했을 때의 `n` 값을 return 해줌.
'''
