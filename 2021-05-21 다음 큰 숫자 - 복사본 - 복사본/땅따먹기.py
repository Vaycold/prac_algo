def one(n) :
    return len([i for i in list(bin(n)[2:]) if i=='1']) # 1의 갯수를 판별하는 함수
def solution(n) :
    t = one(n)
    answer = n+1
    k = one(answer)
    
    while  t != k : 
        answer += 1
        k = one(answer)
        
    return answer
