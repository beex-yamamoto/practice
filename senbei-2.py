# 50分かかった

N, M = map(int, input().split())
A, B, C = map(int, input().split())

for b in range(N + 1):
    # print(f'b = {b}')
    y = C * N - M - (C - B) * b
    # print(f'y {y}')
#    if y < 0:
#        print(f'j探索終了 {j}')
#        break
    if C == A:
        if C == B:
            if C == 0:
                print(f'0 {N} 0')
                exit(0)
            if b * B == M:
                print(f'0 {b} 0')
                exit(0)
            break
        if b * (C - B) == y:
            print(f'0 {N} 0')
    if y % (C - A) > 0:
        # print('iが整数でない')
        continue
    a = y // (C - A)
    # print(f'i = {i}')
    if a >= 0 and N - a - b >= 0:
        print(f'{a} {b} {N - a - b}')
        exit(0)
print('-1 -1 -1')

