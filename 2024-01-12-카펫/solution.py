
def solution(brown, yellow):
       
    for i in range(1, int(yellow**(1/2))+1) :
        if yellow % i == 0 : 
            width, height = yellow // i, i
            if width*2 + height*2 + 4 == brown :
                return [width+2,height+2]
'''
- 직사각형 모양이므로 안에 있는 노란색의 갯수의 제곱근 만큼만 반복한다.
- e.g) 노란색 4개 ⇒ 2x2 형태로 안에 있기 때문에 2일 때까지만 확인하면 됨.
- 1부터 반복해서 노란색이 i의 배수일 때 그 때의 노란색 카펫의 가로, 세로를 구한다.
- 바깥을 감싸기 위해서 갈색카펫의 총 갯수는 노란색 카펫 가로길이 x 2 ( 위 아래) + 노란색 카펫 세로길이 x 2 (좌 우) + 4(모서리4개)가 되어야 한다.
'''
