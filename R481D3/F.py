from bisect import bisect_left


def main():
    n, k = map(int, input().split())
    skill = [int(x) for x in input().split()]
    sorted_skill = sorted(skill)
    inferior = [bisect_left(sorted_skill, sk) for sk in skill]

    for _ in range(k):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if skill[x] < skill[y]:
            inferior[y] -= 1
        if skill[y] < skill[x]:
            inferior[x] -= 1

    print(*inferior)


if __name__ == '__main__':
    main()
