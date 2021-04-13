def solution(N, stages):
    result = {}
    length = len(stages)              #총 사람의 수
    for stage in range(1, N+1) :
        if length == 0 :
            result[stage] = 0
        else :
            ct = stages.count(stage) # 그 'stage' 머무르게 된 사람의 수
            result[stage] = ct / length
            length -= ct
    result = sorted(result, key = lambda x : result[x], reverse=True)        
    return result




'''
Self Feedback
문제를 이해하는 데 시간이 많이 소모된 것 같다. 
완벽하게 구현하려고 하다보니 수식이 더 많아지고 가감하는 데에서 시간이 많이 소모된 듯 하다.
단순하게 생각하는 것도 하나의 방식이 될 수 있을 것 같다. 

Self Keyword

stages.count(), 딕셔너리 용법을 익혀야 겠다. 

'''
