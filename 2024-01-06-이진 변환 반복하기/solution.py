def solution(s):
    
    n = len(s)
    ct, zero_ct = 0, 0
    
    while s != '1' :
        zero = s.count('0')
        zero_ct += zero
        target_num = n - zero
        s = bin(target_num)[2:]
        n = len(s)
        ct += 1
        
    return ct,zero_ct

'''
주어진 문제 그대로 풀면 되는 쉬운 문제!
'''
