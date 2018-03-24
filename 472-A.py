def findq(s, i):
    start = s.find('?', i)
    if start != -1:
        stop = start
        while stop < len(s) and s[stop] == '?':
            stop += 1
        return start, stop - start
    else:
        return None, None


def main():
    n = int(input())
    s = input()

    # does it obey the rule now ?
    no = False
    for x in 'CMY':
        if x * 2 in s:
            no = True
    if no:
        print('No')
        return

    else:
        # is there more than two options?
        two_ways = False
        i, l = findq(s, 0)
        while i is not None:
            if l == 1 and 0 <= i-1 and i+l < n and s[i-1] != s[i+l]:
                pass
            else:
                two_ways = True
                break
            i, l = findq(s, i+l)
        if two_ways:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
