nums = [4, 1, 13, 7, 0, 2, 8, 11, 3]

def build_children(nums):
    n = len(nums)
    children = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                children[i].append(j)

    return children


def dfs_all_paths(start, children, nums):
    result = []
    def dfs(path):
        last = path[-1]
        extended = False
        for nxt in children[last]:
            if nums[nxt] > nums[last]:
                extended = True
                dfs(path + [nxt])
        if not extended:
            result.append(path)
    dfs([start])
    return result


def find_all_LIS(nums):
    children = build_children(nums)
    all_paths = []

    for i in range(len(nums)):
        all_paths.extend(dfs_all_paths(i, children, nums))

    val_paths = [[nums[i] for i in path] for path in all_paths]
    max_len = max(len(path) for path in val_paths)
    LIS = [p for p in val_paths if len(p) == max_len]
    return LIS

LIS = find_all_LIS(nums)

print("Monotonically Increasing Subsequences via Tree DFS:")
for seq in LIS:
    print(seq)
