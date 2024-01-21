def solution(orders, course):
    
    from itertools import combinations
    menu = []
    for c in course :
        c_dict = {}
        for order in orders :
            for comb in combinations(order,c) :
                comb = ''.join(sorted(comb)) 
                
                if comb not in c_dict :
                    c_dict[comb] = 1
                else :
                    c_dict[comb] += 1
        course_count = sorted(c_dict.items() , key = lambda x : x[1], reverse=True)
        if course_count:
            max_value = course_count[0][1]
            sub_answer = []
            if max_value == 1:
                continue
            else :
                for food, ct in course_count :
                    if ct >= max_value :
                        sub_answer.append(food)
                    else :
                        break
            menu.extend(sub_answer)
                
        
    return sorted(menu)
