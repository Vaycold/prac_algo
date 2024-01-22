def solution(want, number, discount):
    
    answer = 0
    for i in range(len(discount)-9) :
        
        for w,n in zip(want,number) :
            if discount[i : 10+i].count(w) != n :
                break
        else :
            answer += 1
            
    return answer
'''
- 주어진 리스트를 차례대로 10개씩 보면서 해당 want의 품목이 number갯수랑 다르면 바로 반복문을 종료시킨다.
- 만약 반복문이 종료되지 않고 끝까지 돌았을 때 answer값을 1씩 추가한다.
- 주어진 문제 그대로 구현하면 되는 문제
'''
