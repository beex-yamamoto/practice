# 40分

N, M = map(int, input().split())
p = [0]*(M + 1)
# a = [0]*(N + 1)
# b = [0]*(N + 1)
for j in range(1, N + 1):
    a, b = map(int, input().split())
    # print(f'j={j}')
    if j < 3:
        continue
    for n in range(1, j - 1):
        # print(f'j={j} a={a} b={b} n={n}')
        if a + b + n == j:
            print(f'{j}番目の人は{a+b}秒後に{n}番目のピンにあたるかも ')
            p[n] = p[n] + 1
# print(p)
# 倒れた本数＝M本-1回も当たらなかったピンの本数
print(M - p.count(0) + 1)

