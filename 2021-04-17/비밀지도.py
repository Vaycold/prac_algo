def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2) :
        # 비트연산자'|' 사용 or의미임.
        # rjust는 n칸만큼 할당해서 우측으로 밀착시키는 개념
        #  - 나머지는 0으로 채움.
        result = str(bin(i|j))[2:].rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(result)
    return answer