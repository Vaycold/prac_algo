def solution(skill, skill_trees):
    Dict = {}
    lvg = 0
    answer = 0
    ct = 0
    for idx, value in enumerate(skill) :
        Dict[value] = idx
    for Skill in skill_trees :
        for i in Skill :
            ct += 1
            t = Dict.get(i,-1)
            if t > lvg :
                ct = 0
                lvg = 0
                break
            elif t == lvg :
                lvg += 1
            if ct == len(Skill) :
                answer += 1
                ct = 0
                lvg = 0
                break
            
    return answer
