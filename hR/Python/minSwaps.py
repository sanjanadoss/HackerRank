def dfs(vec, vis, node, compSize):
    vis[node] = True
    compSize[0] += 1
    for x in vec[node]:
        if not vis[x]:
            dfs(vec, vis, x, compSize)

def minimumSwaps(a, n):
    aux = [*enumerate(a)]
    aux.sort(key=lambda it: it[1])
    vis = [False] * (n + 1)
    vec = [[] for i in range(n + 1)]
    for i in range(n):
        vec[aux[i][0] + 1].append(i + 1)
    ans = 0
    for i in range(1, n + 1):
        compSize = [0]
        if not vis[i]:
            dfs(vec, vis, i, compSize)
            ans += compSize[0] - 1
    return ans

#-----------------------------------------------------------------------------

def swap_count(input_arr):
   pos = sorted(list(enumerate(input_arr)), key=lambda x: x[1])
   cnt = 0

   for index in range(len(input_arr)):
      while True:
         if (pos[index][0] == index):
            break
         else:
            cnt += 1
            swap_index = pos[index][0]
            pos[index], pos[swap_index] = pos[swap_index], pos[index]

   return cnt

def solve(input_arr):
   return min(swap_count(input_arr), swap_count(input_arr[::-1]))

nums = [2, 5, 6, 3, 4]
print(solve(nums))