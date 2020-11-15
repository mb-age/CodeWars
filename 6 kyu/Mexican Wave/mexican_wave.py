def wave(w):
    return [w[:i] + w[i].upper() + w[i + 1:] for i in range(len(w)) if w[i].isalpha()]
