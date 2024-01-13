def solution(n,words) :
    cur = words[0][0]
    word_list = []
    
    for idx, word in enumerate(words) :
        if word[0] == cur and (word not in word_list):
            cur = word[-1]
            word_list.append(word)
        else :
            return (idx % n)+1, (idx // n)+1
    return 0, 0

'''
- 끝말잇기 규칙이 맞을 경우(`word[0] == cur` ; 첫 번째 단어와 끝단어가 맞을 때, `word not in word_list`; 현재 단어가 중복되지 않았을 때) 끝 단어를 맞춰야 될 단어로 초기화하고 해당 단어를 단어리스트에 넣는다
- 규칙이 아닐 경우 틀린 사람의 번호와 차례를 나타내야 되는데 번호는 1, 2, 3,..n, 1.,2,3,…,n 까지 반복되므로 현재 숫자의 나머지와 같고, 차례는 현재 숫자의 몫과 같다.(1,1,1,1 ;n개)  (2,2,2,2 ;n개) (3,3,3,3 ;n개)
'''
