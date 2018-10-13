def scalar(k1, n):
    k2 = [0] * 3
    for i in range(3):
        k2[i] = k1[i] * n[i]
    return k2


def minus(k1, n):
    k2 = [0] * 3
    for i in range(3):
        k2[i] = k1[i] - n[i]
    return k2
    
    def MultiplyByNumber (k1, n):
    k2 = [0] * 3
    for i in range(3):
        k2[i] = k1[i] * n
    return k2
