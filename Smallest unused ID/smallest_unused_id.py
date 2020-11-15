def next_id(arr):
    return min(i for i in range(len(arr)+1) if i not in arr) if arr else 0
