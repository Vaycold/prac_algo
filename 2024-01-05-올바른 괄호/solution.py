def solution(s) :
    stack = []
    for gwalho in s :
        if gwalho == '(':
            stack.append('(')
        else :
            if not stack : return False
            else : stack.pop()
    return not bool(stack)
'''
stack의 자료구조를 활용하는문제

괄호가 ( 라면 무조건 스택에 집어넣고
괄호가 ) 라면 스택의 맨 마지막에 있는 값을 삭제(pop)한다. 
근데 만약 스택이 빈 상태에서 )가 나오게 되면 괄호가 닫힐 수 없으므로 바로 False를 return 한다.

끝까지 했을 때 스택이 비어 있다면(bool(stack) = False) 모든 괄호가 열고 닫힌 것이기 때문에 not False가 되어 True가 되고
끝까지 했을 때 스택이 남아 있다면(bool(stack) = True) ( 괄호가 아직 남아 안닫힌 것이기 떄문에 not True가 되어 False가 return된다.

'''
