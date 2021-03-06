# n nodes, n - 1 edges, no possibility for loop
# so no need of maintaining a vis array, it'd not visit nodes previously visited
# as long as you don't go along the edge back which leads you to the current node


from collections import deque
from array import array


def main():
    n = int(input())
    # don't use hash table
    neis = [[] for i in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        neis[u].append(v)
        neis[v].append(u)

    def fake_dfs(start_point):
        nonlocal neis

        # vis = [0 for i in range(n + 1)]  # vis[i] -- the next node i is going to visit is neis[vis[i]]
        # nodes = [1 for i in range(n + 1)]  # nodes[i] -- the number of nodes 'belong to' i(included i)
        # pre = [None for i in range(n + 1)]  # pre[i] -- the node which leads to node i in fake dfs process
        vis = array('I', (0 for _ in range(n + 1)))
        nodes = array('I', (1 for _ in range(n + 1)))
        pre = array('I', (0 for _ in range(n + 1)))
        cut = 0

        q = deque()
        q.append(start_point)
        pre[start_point] = start_point

        while len(q) > 0:
            top = q[-1]

            if vis[top] < len(neis[top]):
                nei = neis[top][vis[top]]
                vis[top] += 1
                if nei != pre[top]:
                    q.append(nei)
                    pre[nei] = top
            else:
                if top != start_point:
                    nodes[pre[top]] += nodes[top]
                    if nodes[top] & 1 == 0:
                        cut += 1
                q.pop()

        if nodes[1] & 1 == 0:
            print(cut)
        else:
            print(-1)

    fake_dfs(1)


if __name__ == '__main__':
    main()
