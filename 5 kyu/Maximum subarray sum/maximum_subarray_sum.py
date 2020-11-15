def max_sequence(a):
    return max(map(sum,[[0]]+[a[i:j] for i in range(len(a)) for j in range(i+1,len(a)+1)]))
