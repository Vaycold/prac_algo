def solution(babbling):
    answer = 0
    for babble in babbling :
        target = babble
        while target :
            if (target.startswith('aya')) or (target.startswith('ye')) or (target.startswith('woo')) or (target.startswith('ma')) :
                if target.startswith('aya') :
                    target = target.replace('aya','')
                    if len(target) == 0 :
                        answer += 1
                elif target.startswith('ye') :
                    target = target.replace('ye','')
                    if len(target) == 0 :
                        answer += 1
                elif target.startswith('woo') :
                    target = target.replace('woo','')
                    if len(target) == 0 :
                        answer += 1
                elif target.startswith('ma') :
                    target = target.replace('ma','')
                    if len(target) == 0 :
                        answer += 1
            else : break
                
                            
        
    return answer
