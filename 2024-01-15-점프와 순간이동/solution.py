def solution(N) :
    answer = 0
    while N != 0 :
        if not N % 2  :
            N /= 2
        else :
            N -=1 
            answer += 1
    return answer

'''
- 주어진 N에서 0으로 이동한다고 생각하자.
- 최소로 이동해야 하기 때문에 2로 나눌 수 있으면 나누고 없으면 1을 뺀다.
- 2의 승수일때는 1칸만 움직이고 순간이동하면 되기 때문에 1이 된다.
- 2의 승수가 아닐 때에는 1칸 이동하고 이동 횟수 1을 더해준다.
'''
