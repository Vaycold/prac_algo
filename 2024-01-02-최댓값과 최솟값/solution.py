def solution(s) :
    s = list(map(str,sorted(list(map(int,s.split(' '))))))
    return f'{s[0]} {s[-1]}' 
'''
1. 주어진 문자열 데이터를 공백(' ')으로 나눈다. eg) "1 2 3 4" ->["1", "2", "3", "4"]
2. 정렬을 하기 위해 각 원소에 대해 int 함수를 mapping 시킨다 .
3. 정렬을 한 다음 문자열(str)로 다시 mapping 시킨다.
4. 첫 번째(최솟값)과 마지막 값(최댓값)을 return 한다.
'''
