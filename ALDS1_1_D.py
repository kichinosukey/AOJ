import numpy as np

def diff(buy, sell, rate=1):
    return (sell - buy) * rate


if __name__ == "__main__":
    
    tx = [6, 5, 3, 1, 3, 4, 3]
    tx_02 = [3, 4, 3, 2]
    length = tx[0]
    tx = tx[1:]

    # length = 10000000
    # tx = list(np.random.randint(1, 10, length))
    maxv = -2*10**9
    minv = tx[0]

    for v in tx:
        maxv = max(maxv, v)
        minv = min(minv, v)
    print(maxv - minv)