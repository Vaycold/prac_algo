def solution(x):
    sum_ = sum([int(i) for i in str(x)])

    return x % sum_ ==0
