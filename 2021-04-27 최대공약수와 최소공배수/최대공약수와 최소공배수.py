def solution(n, m):
    n_list = []
    m_list = []
    answer = []
    for i,j in zip(list(range(1,n+1)), list(range(1,m+1))) :
                   if n % i == 0 :
                        n_list.append(i)
                   if m % j == 0 :
                        m_list.append(j)
    g = max(list(set(n_list) & set(m_list)))
    answer.append(g)            
    answer.append(n*m/g)
