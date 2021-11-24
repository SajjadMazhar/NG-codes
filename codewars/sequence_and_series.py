def get_score(n):
    summation = 0
    for i in range(n):
        summation = summation + 50*(i+1)
    return summation

get_score(2)
