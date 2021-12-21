A = list(map(int, input().split()))

A.remove(max(A))
A.remove(min(A))
print(A[0])

