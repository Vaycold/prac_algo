def solution(dirs) :
    
    i, j = 0, 0
    dirs_dictionary = { 'U' : (-1,0), 'L' : (0,-1), 'D' : (1,0), 'R' : (0,1) }
    move_history = set()
    
    for dir in dirs :
        
        di, dj = dirs_dictionary[dir]
        new_i, new_j = i+di, j+dj
        
        if (abs(new_i) <= 5) and (abs(new_j) <= 5) :
            move_history.add((i,j,new_i,new_j))
            move_history.add((new_i,new_j,i,j))
            i, j = new_i,new_j
            
    return int(len(move_history)/2)

'''
- 상하좌우 이동을 나타낼 수 있는 딕셔너리를 먼저 만든다.
- 이동기록을 체크할 수 있는 집합(set)을 만든다.
- 상하좌우를 이동하면서 새로 이동할 곳이 5 x 5 영역 내에 있는 먼저 체크한다.
- 이동기록을 체크하는 집합에는 출발좌표, 도착좌표가 들어가는데 돌아오는 길 또한 같이 카운트하기 때문에 도착좌표, 출발좌표 또한 이동기록에 집어넣는다.
- 경로가 두번 중복되기 때문에 2로 나눠 준다.
'''
