def solution(n) :
    answer = 1
    for i in range(1,int(n/2)+1) :
        ct = 0 
        for num in range(i, n) :
            ct += num 
            if ct == n :
                answer += 1                
                break
            elif ct > n :
                break
    return answer
  '''
  절반까지만 반복을 돌아도 상관없기 때문에 주어진 숫자의 (n/2)까지만 반복하게끔한다.
  그리고 자기 자신일 때의 경우를 카운트하기 위하여 
  시작 answer 값을 1로 주고 시작한다.
  '''
