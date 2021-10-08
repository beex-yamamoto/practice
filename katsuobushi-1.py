# Aをソートして、大小の2グループに分ける
# 大小それぞれ同じ位置から1つ取り出してXi-Yiを計算して、その最小値がm
# 解答 25分


N = int(input())
A = list(map(int, input().split()))
A.sort()

m = 1000000000  # sys.maxsizeでも

for i in range(N):
    d = A[N + i] - A[i]
    # print(d)
    if d < m:
        m = d
# print("----")
print(m)
