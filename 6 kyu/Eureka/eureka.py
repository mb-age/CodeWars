def sum_dig_pow(a, b):
    return [k for k in range(a,b+1) if sum(int(j)**i for i,j in enumerate(str(k),1)) == k]
