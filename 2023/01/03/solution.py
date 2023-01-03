def solution(my_string):
    init = 0                        # 숫자의 시작을 나타냄
    num_list = []                   # 숫자만 담을 거임
    for char in my_string :
        if not char.isdigit() :         # 주어진 string이 숫자열이 아님??
            init = 0                          # 그러면 그냥 pass(그전 string이 숫자 시작이었어도 문자열을 만나는 순간 0으로 변환)
            
        else :                          # 주어진 srting이 숫자열임??
            if init == 0 :                    # 숫자의 시작임??
                num_list.append(char)               # 숫자 리스트에 넣음
                init = 1                            # 숫자의 시작이 아님을 표시
            
            else  :                           # 숫자의 시작이 아님 == 바로 앞에 숫자가 있었음
                num = num_list[-1] + char        # 마지막에 넣은 값 + 또 찾은 숫자값 
                num_list = num_list[:-1]         # 마지막에 넣은 값을 리스트에서 지움
                num_list.append(num)             # 새로만든 숫자를 리스트에 집어 넣음
    return sum([int(a) for a in num_list])
solution(my_string)
