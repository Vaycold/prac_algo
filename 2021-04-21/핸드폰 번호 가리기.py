def solution(phone_number):
    answer = str(phone_number)[:-4].replace(str(phone_number)[:-4],'*'*len(str(phone_number)[:-4]))+str(phone_number)[-4:]
    
    return answer
