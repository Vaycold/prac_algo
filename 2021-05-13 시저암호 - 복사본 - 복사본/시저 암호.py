import string
a_l = string.ascii_lowercase
a_u = string.ascii_uppercase
num = list(range(1,27))
dict_1 = {}
dict_2 = {}
for key, value in zip(a_l, num) :
    dict_1[key] = value # Lowercase
for key, value in zip(a_u, num) :
    dict_2[key] = value # Uppercase
def solution(word, n) :
    answer =''
    for s in word :
        if s == ' ' :
            answer = answer + ' '
            continue
        try :
            idx = dict_1[s] + n
            if idx > 26 : 
                idx = idx - 26
            for key, value in dict_1.items() :
                if value == idx :
                    answer = answer + key
        except :
            idx = dict_2[s] + n
            if idx > 26 : 
                idx = idx - 26
            for key, value in dict_2.items() :
                if value == idx :
                    answer = answer + key
        
    return answer
