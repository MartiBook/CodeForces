# just need to use only max prime factor p_max of x2, because (x2-p_max, x2] contains all possible x1


def prime_factors(n):
    f = 2
    while f * f <= n:
        while n % f == 0:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n


x2 = int(input())
max_p_x2 = max([x for x in prime_factors(x2)])
ans = float('Inf')
for x1 in range((x2 - max_p_x2 + 1), x2 + 1):
    max_p_x1 = max([x for x in prime_factors(x1)])
    if x1 - max_p_x1 > 0:
        ans = min(ans, x1 - max_p_x1 + 1)
    else:
        ans = min(ans, x1)
    if ans < x1 // 2:
        break

print(ans)
