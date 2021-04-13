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

