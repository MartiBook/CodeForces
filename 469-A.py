l, r, a = map(int, input().split())

if a > abs(l - r):
    ans = max(l, r) + (a - abs(l - r)) // 2
else:
    ans = min(l, r) + a

print(ans * 2)
