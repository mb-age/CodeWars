def pick_peaks(arr):
    d = {'pos': [], 'peaks': []}
    for i, j in enumerate(arr[1:-1], 1):
        if arr[i-1] < j:
            if j > arr[i+1]:
                d['pos'].append(i)
                d['peaks'].append(j)
            elif j == arr[i+1]:
                a = 0
                while j == arr[i+1] and i<len(arr)-2:
                    i += 1
                    a += 1
                    if j > arr[i+1]:
                        d['pos'].append(i-a)
                        d['peaks'].append(j)
    return d
